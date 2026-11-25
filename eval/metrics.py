"""
Automatic metrics for cited, source-grounded answers.

No reference answers are needed: every metric is computed from the
answer and the passages the model was given.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from prompts import REFUSAL  # noqa: E402

CITATION = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")
THINK_BLOCK = re.compile(r"<think>.*?</think>", re.DOTALL)
# Split after sentence punctuation, but keep a trailing "[n]" attached.
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?!\[)")
WORD = re.compile(r"[a-z0-9]+")

REFUSAL_PATTERNS = [
    "do not contain the answer",
    "does not contain the answer",
    "don't contain the answer",
    "doesn't contain the answer",
    "not contain information",
    "no information about",
    "not mentioned in the sources",
    "sources do not",
    "sources don't",
]

STOPWORDS = set("""
a an the and or but if then than so of to in on at by for with from as
is are was were be been being it its this that these those there their
they them he she his her we you your our i not no can could would should
may might will which who whom what when where why how also into about
over under more most such other some any each many much very just only
has have had do does did up out one two all both between because while
""".split())


def strip_thinking(text):
    """
    Remove <think> blocks some models emit. Returns (clean, had_thinking).
    """

    had_thinking = "<think>" in text
    clean = THINK_BLOCK.sub("", text)
    clean = clean.replace("<think>", "").replace("</think>", "")
    return clean.strip(), had_thinking


def is_refusal(text):
    lowered = text.lower()
    return any(pattern in lowered for pattern in REFUSAL_PATTERNS)


def citations_in(text):
    numbers = []
    for group in CITATION.findall(text):
        numbers.extend(int(n) for n in group.split(","))
    return numbers


# A period after these doesn't end a sentence ("Robert T. Paine", "Nix v. Hedden").
_NO_BREAK_AFTER = re.compile(
    r"(\b[A-Z]|\bv|\bvs|\be\.g|\bi\.e|\bDr|\bMr|\bMrs|\bMs|\bSt|\bNo|\bapprox|\bca)\.$"
)


def split_sentences(text):
    pieces = [s.strip() for s in SENTENCE_SPLIT.split(text) if s.strip()]
    merged = []
    for piece in pieces:
        if merged and _NO_BREAK_AFTER.search(merged[-1]):
            merged[-1] = f"{merged[-1]} {piece}"
        else:
            merged.append(piece)
    return merged


def content_words(text):
    return [
        w for w in WORD.findall(text.lower())
        if len(w) > 3 and w not in STOPWORDS
    ]


def question_overlap(answer, question):
    """
    Share of the question's content words that appear in the answer
    (stem match on the first 5 letters). Near 0 means the answer is
    probably about something else, e.g. a copied prompt example.
    """

    def stems(text):
        # Keep 3-letter words too, so acronyms like "VPN" count.
        return {w[:5] for w in WORD.findall(text.lower())
                if len(w) >= 3 and w not in STOPWORDS}

    asked = stems(question)
    if not asked:
        return None
    return len(asked & stems(answer)) / len(asked)


def score_answer(answer, passages, answerable, question=None):
    """
    Score one answer against the passages that were in the prompt.
    """

    text, had_thinking = strip_thinking(answer)
    # A cited answer that notes a gap ("The sources do not say X") is a
    # partial answer, not a refusal.
    refused = is_refusal(text) and not citations_in(text)
    n_passages = len(passages)

    cited = citations_in(text)
    citation_valid = all(1 <= n <= n_passages for n in cited)

    result = {
        "refused": refused,
        "behaviour_correct": refused != answerable,
        "exact_refusal": text == REFUSAL,
        "had_thinking": had_thinking,
        "words": len(text.split()),
        "citations": cited,
        "citation_valid": citation_valid,
        "citation_coverage": None,
        "groundedness": None,
        "question_overlap": None,
        "off_topic": False,
    }

    # Citation coverage and groundedness only apply to real answers.
    if refused or not text:
        return result

    sentences = split_sentences(text)
    passage_words = [set(content_words(p["text"])) for p in passages]
    all_words = set().union(*passage_words) if passage_words else set()

    covered = 0
    support_scores = []

    for sentence in sentences:
        sentence_cites = [
            n for n in citations_in(sentence) if 1 <= n <= n_passages
        ]
        if citations_in(sentence):
            covered += 1

        words = content_words(CITATION.sub("", sentence))
        if not words:
            continue

        # Check words against the cited passages; uncited sentences
        # are checked against all passages (lenient).
        if sentence_cites:
            source = set().union(*(passage_words[n - 1] for n in sentence_cites))
        else:
            source = all_words

        support_scores.append(sum(w in source for w in words) / len(words))

    if question:
        overlap = question_overlap(text, question)
        result["question_overlap"] = overlap
        result["off_topic"] = overlap is not None and overlap == 0

    result["citation_coverage"] = covered / len(sentences) if sentences else 0.0
    result["groundedness"] = (
        sum(support_scores) / len(support_scores) if support_scores else 0.0
    )

    return result


def mean(values):
    values = [v for v in values if v is not None]
    return sum(values) / len(values) if values else None


def aggregate(rows):
    """
    Summarise per-item scores for one model.
    """

    answerable = [r for r in rows if r["answerable"]]
    unanswerable = [r for r in rows if not r["answerable"]]
    answered = [r for r in answerable if not r["refused"]]

    return {
        "items": len(rows),
        "behaviour_accuracy": mean([r["behaviour_correct"] for r in rows]),
        "answer_rate": mean([not r["refused"] for r in answerable]),
        "refusal_rate_unanswerable": mean([r["refused"] for r in unanswerable]),
        "exact_refusal_unanswerable": mean(
            [r.get("exact_refusal", False) for r in unanswerable]
        ),
        "citation_validity": mean([r["citation_valid"] for r in answered]),
        "answers_with_citations": mean([bool(r["citations"]) for r in answered]),
        "citation_coverage": mean([r["citation_coverage"] for r in answered]),
        "groundedness": mean([r["groundedness"] for r in answered]),
        "off_topic_answers": sum(bool(r.get("off_topic")) for r in answered),
        "mean_words": mean([r["words"] for r in answered]),
        "thinking_leaks": sum(r["had_thinking"] for r in rows),
        "mean_latency_s": mean([r["latency_s"] for r in rows]),
        "prompt_tok_per_s": mean([r["prompt_tok_per_s"] for r in rows]),
        "gen_tok_per_s": mean([r["gen_tok_per_s"] for r in rows]),
        "errors": sum(bool(r.get("error")) for r in rows),
    }

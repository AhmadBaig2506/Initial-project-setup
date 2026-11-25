"""
Single source of truth for the answer-generation prompt.

Used by the app, dataset generation, training and evaluation so every
stage sees exactly the same input format.

Prompt variants (pick with build_messages(..., variant=...)):
    v1          baseline instructions (default; used for all baseline results)
    v2-oneshot  v1 + one worked example showing citations and a refusal
    v3-3shot    v1 + 3 examples (2 answers, 1 refusal)
    v5-5shot    v1 + 5 examples (2 answers, 2 refusals incl. on-topic, 1 partial)
"""

import re

REFUSAL = "The sources do not contain the answer."

SYSTEM_PROMPT = (
    "You are a research assistant. Answer the question using ONLY the "
    "numbered sources provided. Do not use any outside knowledge.\n"
    "Rules:\n"
    "- Cite every sentence with the source number(s) it comes from, "
    "like [1] or [2][3].\n"
    "- Keep the answer to 2-5 sentences.\n"
    f"- If the sources do not contain the answer, reply exactly: {REFUSAL}"
)

ONESHOT_EXAMPLE = (
    "\n\nExample.\n"
    "Sources:\n"
    "[1] Tides explained\n"
    "Tides are caused mainly by the Moon's gravity pulling on Earth's oceans. "
    "Most coastlines see two high tides and two low tides each day.\n"
    "[2] The Sun and tides\n"
    "The Sun also affects tides. When the Sun and Moon line up, their combined "
    "pull creates larger spring tides.\n"
    "Question: What causes ocean tides?\n"
    "Answer: Ocean tides are caused mainly by the Moon's gravity pulling on "
    "Earth's oceans [1]. The Sun also contributes, and when the Sun and Moon "
    "line up their combined pull creates larger spring tides [2]. Most "
    "coastlines get two high tides and two low tides each day [1].\n\n"
    "Question: Who discovered tides?\n"
    f"Answer: {REFUSAL}\n\n"
    "Note how every sentence ends with its citation, and the refusal is "
    "copied exactly."
)

# Few-shot examples. Each has its own sources and a different topic from
# every test question, and is labelled so models don't reuse its content.
_TIDES = (
    "[1] Tides explained\n"
    "Tides are caused mainly by the Moon's gravity pulling on Earth's oceans. "
    "Most coastlines see two high tides and two low tides each day.\n"
    "[2] The Sun and tides\n"
    "The Sun also affects tides. When the Sun and Moon line up, their combined "
    "pull creates larger spring tides."
)
_BEES = (
    "[1] From nectar to honey\n"
    "Worker bees collect nectar from flowers and store it in a special honey "
    "stomach. Enzymes in the stomach begin breaking the sugars down.\n"
    "[2] Inside the hive\n"
    "Back at the hive, bees pass the nectar between them and deposit it in wax "
    "cells. They fan it with their wings until most of the water evaporates, "
    "then seal the cell with wax."
)
_BRIDGE = (
    "[1] Golden Gate Bridge history\n"
    "The Golden Gate Bridge opened to traffic in 1937 after four years of "
    "construction. Its chief engineer was Joseph Strauss.\n"
    "[2] Bridge colour\n"
    "The bridge is painted a colour called International Orange, chosen "
    "because it stays visible in fog."
)

FEW_SHOT = [
    # 1: answer citing several sources
    (_TIDES, "What causes ocean tides?",
     "Ocean tides are caused mainly by the Moon's gravity pulling on Earth's "
     "oceans [1]. The Sun also contributes, and when the Sun and Moon line up "
     "their combined pull creates larger spring tides [2]. Most coastlines get "
     "two high tides and two low tides each day [1]."),
    # 2: answer from two sources about a process
    (_BEES, "How do bees make honey?",
     "Worker bees collect nectar and store it in a honey stomach, where enzymes "
     "start breaking down the sugars [1]. At the hive they pass the nectar "
     "between them, place it in wax cells and fan it with their wings until "
     "most of the water evaporates [2]. They then seal each cell with wax [2]."),
    # 3: refusal, sources are on an unrelated topic
    (_BRIDGE, "How do vaccines work?", REFUSAL),
    # 4: refusal, sources are on the same topic but lack the fact
    (_BEES, "How many bees live in a typical hive?", REFUSAL),
    # 5: partial answer, one part is covered and one is not
    (_BRIDGE, "When did the Golden Gate Bridge open and how much did it cost?",
     "The Golden Gate Bridge opened to traffic in 1937 [1]. "
     "The sources do not say how much it cost."),
]

# Order used for the 3-shot variant: two answers and one refusal.
THREE_SHOT = [FEW_SHOT[0], FEW_SHOT[1], FEW_SHOT[2]]


def _examples_block(examples):
    parts = [
        "\n\nThe examples below show the required format. Their topics are "
        "unrelated to the real question: never copy their content."
    ]
    for number, (sources, question, answer) in enumerate(examples, start=1):
        parts.append(
            f"\n\n### Example {number}\nSources:\n{sources}\n"
            f"Question: {question}\nAnswer: {answer}"
        )
    parts.append(
        "\n\n### End of examples\nEvery sentence ends with its citation. "
        "Refusals are copied exactly. If only part of the question is covered, "
        "answer that part and say which part the sources do not cover."
    )
    return "".join(parts)


VARIANTS = {
    "v1": SYSTEM_PROMPT,                                   # 0-shot
    "v2-oneshot": SYSTEM_PROMPT + ONESHOT_EXAMPLE,         # 1-shot (tides + refusal)
    "v3-3shot": SYSTEM_PROMPT + _examples_block(THREE_SHOT),
    "v5-5shot": SYSTEM_PROMPT + _examples_block(FEW_SHOT),
}
DEFAULT_VARIANT = "v1"

MAX_PASSAGE_WORDS = 180
MAX_TOTAL_WORDS = 1000


def format_passages(passages):
    """
    Number passages [1]..[k], truncating to keep the prompt small.
    """

    sections = []
    words_used = 0

    for index, passage in enumerate(passages, start=1):
        remaining = MAX_TOTAL_WORDS - words_used
        if remaining <= 0:
            break

        words = passage["text"].split()[:min(MAX_PASSAGE_WORDS, remaining)]
        words_used += len(words)

        sections.append(f"[{index}] {passage['title']}\n{' '.join(words)}")

    return "\n\n".join(sections)


def build_messages(question, passages, variant=DEFAULT_VARIANT):
    """
    Chat messages for the model (system + user).
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    user = (
        f"Sources:\n\n{format_passages(passages)}\n\n"
        f"Question: {question}"
    )

    return [
        {"role": "system", "content": VARIANTS[variant]},
        {"role": "user", "content": user},
    ]


_REFUSAL_HINTS = re.compile(
    r"(sources?|passages?|provided (text|information)).{0,40}"
    r"(do not|does not|don't|doesn't|not) (contain|include|mention|provide|have)",
    re.IGNORECASE,
)


def normalize_refusal(answer, max_words=30):
    """
    Replace a paraphrased refusal with the exact REFUSAL sentence.

    Only short answers without citations are rewritten, so a real answer
    that mentions a gap ("the sources do not give a date, but ... [2]")
    is left alone.
    """

    text = answer.strip()
    if text == REFUSAL:
        return text

    short = len(text.split()) <= max_words
    cited = re.search(r"\[\d+", text)

    if short and not cited and _REFUSAL_HINTS.search(text):
        return REFUSAL

    return text

"""Offline tests: no network access or model file required."""

from unittest.mock import MagicMock, patch

import pytest

import extract
import model
import pipeline
from extract import chunk_text
from rank import rank_chunks, tokenize


def make_doc(text, title="Doc", url="https://example.com"):
    return {"source_id": 1, "chunk_id": 0, "title": title,
            "url": url, "text": text}


# --- chunking ---------------------------------------------------------

def test_chunk_text_overlap():
    words = [f"w{i}" for i in range(500)]
    chunks = chunk_text(" ".join(words), chunk_size=200, overlap=40)

    assert len(chunks) == 3
    assert chunks[0].split()[-40:] == chunks[1].split()[:40]
    assert chunks[-1].split()[-1] == "w499"


def test_chunk_text_short_and_empty():
    assert chunk_text("one two three") == ["one two three"]
    assert chunk_text("") == []


@pytest.mark.parametrize("size,overlap", [(0, 0), (10, 10), (10, -1)])
def test_chunk_text_invalid(size, overlap):
    with pytest.raises(ValueError):
        chunk_text("text", chunk_size=size, overlap=overlap)


# --- ranking ----------------------------------------------------------

def test_tokenize():
    assert tokenize("Sleep-Apnea, CAUSES!") == ["sleep", "apnea", "causes"]


def test_rank_chunks_orders_by_relevance():
    docs = [
        make_doc("cats like milk and sleeping in the sun"),
        make_doc("sleep apnea is caused by airway collapse"),
        make_doc("the stock market rose today"),
    ]

    ranked = rank_chunks("what causes sleep apnea", docs, top_k=2)

    assert len(ranked) == 2
    assert "apnea" in ranked[0]["text"]
    assert ranked[0]["score"] >= ranked[1]["score"]
    assert "score" not in docs[0]  # inputs are not mutated


def test_rank_chunks_validation():
    assert rank_chunks("q", []) == []

    with pytest.raises(ValueError):
        rank_chunks(" ", [make_doc("x")])

    with pytest.raises(ValueError):
        rank_chunks("q", [make_doc("x")], top_k=0)


# --- extraction (mocked HTTP) -----------------------------------------

def fake_response(content_type="text/html", body="<html></html>"):
    response = MagicMock()
    response.headers = {"Content-Type": content_type}
    response.text = body
    response.content = body.encode()
    return response


def test_extract_skips_non_html():
    with patch.object(extract.requests, "get",
                      return_value=fake_response("application/pdf")):
        assert extract.extract_webpage("https://example.com/a.pdf") is None


def test_process_search_results_keeps_order():
    results = [
        {"title": "A", "url": "https://a.com", "snippet": ""},
        {"title": "B", "url": "https://b.com", "snippet": ""},
        {"title": "C", "url": "https://c.com", "snippet": ""},
    ]
    texts = {"https://a.com": "alpha text",
             "https://b.com": None,
             "https://c.com": "gamma text"}

    with patch.object(extract, "extract_webpage", side_effect=texts.get):
        docs = extract.process_search_results(results)

    assert [d["title"] for d in docs] == ["A", "C"]
    assert [d["source_id"] for d in docs] == [1, 3]


# --- model prompt and generation (mocked model) -----------------------

def test_build_prompt_numbers_sources():
    passages = [make_doc("first text", title="First"),
                make_doc("second text", title="Second")]

    prompt = model.build_prompt("Why?", passages)

    assert "[1] First" in prompt
    assert "[2] Second" in prompt
    assert prompt.rstrip().endswith("Answer:")


def test_build_prompt_truncates_long_passages():
    passages = [make_doc("word " * 5000) for _ in range(10)]

    prompt = model.build_prompt("Why?", passages)

    assert prompt.count("word") <= model.MAX_PROMPT_WORDS


def test_generate_answer_with_fake_model():
    fake = MagicMock()
    fake.create_chat_completion.return_value = {
        "choices": [{"message": {"content": " Airway collapse [1]. "}}]
    }

    answer = model.generate_answer("Why?", [make_doc("text")], model=fake)

    assert answer == "Airway collapse [1]."


def test_generate_answer_without_passages():
    assert "No sources" in model.generate_answer("Why?", [])


def test_load_model_missing_file(monkeypatch):
    monkeypatch.setattr(model, "_model", None)

    with pytest.raises(FileNotFoundError):
        model.load_model("does/not/exist.gguf")


# --- pipeline (mocked search) -----------------------------------------

def test_run_research_end_to_end_mocked():
    results = [{"title": "A", "url": "https://a.com", "snippet": ""}]
    docs = [make_doc("sleep apnea is caused by airway collapse")]

    with patch.object(pipeline, "search_web", return_value=results), \
         patch.object(pipeline, "process_search_results", return_value=docs), \
         patch.object(pipeline, "generate_answer", return_value="Answer [1]"):
        result = pipeline.run_research("what causes sleep apnea")

    assert result["sources_found"] == 1
    assert result["answer"] == "Answer [1]"
    assert len(result["passages"]) == 1


def test_run_research_no_results():
    with patch.object(pipeline, "search_web", return_value=[]):
        result = pipeline.run_research("anything")

    assert result["answer"] is None
    assert result["passages"] == []

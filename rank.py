
import json
import re

from rank_bm25 import BM25Okapi


def tokenize(text):
    """
    Convert text into lowercase searchable words.
    """
    return re.findall(r"\b\w+\b", text.lower())


def rank_chunks(question, documents, top_k=5):
    """
    Rank extracted chunks using BM25.
    Return the top_k most relevant chunks.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    if top_k <= 0:
        raise ValueError("top_k must be greater than zero.")

    if not documents:
        return []

    # Tokenize each chunk
    tokenized_corpus = [
        tokenize(doc["text"]) for doc in documents
    ]

    # Build the BM25 index
    bm25 = BM25Okapi(tokenized_corpus)

    # Tokenize the question
    tokenized_query = tokenize(question)

    # Calculate relevance scores
    scores = bm25.get_scores(tokenized_query)

    # Attach each score to its original document
    scored_documents = []

    for document, score in zip(documents, scores):
        scored_document = document.copy()
        scored_document["score"] = float(score)
        scored_documents.append(scored_document)

    # Sort highest score first
    scored_documents.sort(
        key=lambda doc: doc["score"],
        reverse=True
    )

    return scored_documents[:top_k]


def display_ranked_chunks(documents):
    """
    Print the top-ranked passages.
    """

    if not documents:
        print("No ranked chunks available.")
        return

    for position, doc in enumerate(documents, start=1):
        print(f"\n--- Ranked Passage {position} ---")
        print(f"BM25 Score: {doc['score']:.4f}")
        print(f"Title: {doc['title']}")
        print(f"URL: {doc['url']}")
        print(f"Source ID: {doc['source_id']}")
        print(f"Chunk ID: {doc['chunk_id']}")
        print(f"Text: {doc['text'][:500]}...")


def save_ranked_chunks(
    documents,
    filename="ranked_chunks.json"
):
    """
    Save ranked passages to a JSON file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            documents,
            file,
            indent=2,
            ensure_ascii=False
        )


if __name__ == "__main__":
    question = input("Enter your research question: ")

    try:
        with open(
            "chunks.json",
            "r",
            encoding="utf-8"
        ) as file:
            documents = json.load(file)

    except FileNotFoundError:
        print(
            "chunks.json not found. "
            "Run extract.py first."
        )
        raise SystemExit(1)

    ranked = rank_chunks(question, documents, top_k=5)

    display_ranked_chunks(ranked)

    if ranked:
        save_ranked_chunks(ranked)
        print("\nSaved top passages to ranked_chunks.json")
    else:
        print("\nNo passages to save.")

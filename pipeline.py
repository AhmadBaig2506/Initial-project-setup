
import time

from search import search_web
from extract import process_search_results
from rank import rank_chunks


def run_retrieval(question, top_k=5):
    """
    Search, extract, and rank evidence for a question.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    start_time = time.perf_counter()

    # Step 1: Search
    results = search_web(question)

    if not results:
        return {
            "question": question,
            "sources_found": 0,
            "chunks_created": 0,
            "passages": [],
            "elapsed_seconds": time.perf_counter() - start_time
        }

    # Step 2: Extract and chunk
    documents = process_search_results(results)

    # Step 3: Rank
    ranked = (
        rank_chunks(question, documents, top_k=top_k)
        if documents else []
    )

    return {
        "question": question,
        "sources_found": len(results),
        "chunks_created": len(documents),
        "passages": ranked,
        "elapsed_seconds": time.perf_counter() - start_time
    }


if __name__ == "__main__":
    question = input("Enter your research question: ")

    result = run_retrieval(question)

    print(f"\nSources found: {result['sources_found']}")
    print(f"Chunks created: {result['chunks_created']}")
    print(f"Passages selected: {len(result['passages'])}")
    print(f"Time: {result['elapsed_seconds']:.2f} seconds")


import json
import requests
import trafilatura

from search import search_web


def extract_webpage(url):
    """
    Download an HTML webpage and extract its main text.
    """

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "OnDeviceAIResearchPrototype/0.1"
            }
        )

        response.raise_for_status()

        content_type = response.headers.get(
            "Content-Type", ""
        ).lower()

        if "text/html" not in content_type:
            print(f"Skipping non-HTML page: {url}")
            return None

        if len(response.content) > 5_000_000:
            print(f"Skipping large page: {url}")
            return None

        text = trafilatura.extract(
            response.text,
            include_comments=False,
            include_tables=True
        )

        if not text:
            print(f"No readable text found: {url}")
            return None

        return text

    except requests.RequestException as error:
        print(f"Could not fetch {url}: {error}")
        return None


def chunk_text(text, chunk_size=200, overlap=40):
    """
    Divide extracted text into overlapping word chunks.
    """

    if chunk_size <= 0 or not 0 <= overlap < chunk_size:
        raise ValueError("Invalid chunk size or overlap.")

    words = text.split()
    chunks = []

    step = chunk_size - overlap

    for start in range(0, len(words), step):
        chunk_words = words[start:start + chunk_size]

        if not chunk_words:
            break

        chunks.append(" ".join(chunk_words))

        if start + chunk_size >= len(words):
            break

    return chunks


def process_search_results(results):
    """
    Extract and chunk the webpages returned by search.py.
    """

    documents = []

    for source_id, result in enumerate(results, start=1):
        url = result["url"]

        print(f"\nReading: {url}")

        text = extract_webpage(url)

        if not text:
            continue

        chunks = chunk_text(text)

        for chunk_index, chunk in enumerate(chunks):
            documents.append({
                "source_id": source_id,
                "chunk_id": chunk_index,
                "title": result["title"],
                "url": url,
                "text": chunk
            })

    return documents


def save_chunks(documents, filename="chunks.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            documents,
            file,
            indent=2,
            ensure_ascii=False
        )


if __name__ == "__main__":
    question = input("Enter your research question: ")

    results = search_web(question)

    print(f"\nFound {len(results)} search results.")

    documents = process_search_results(results)

    if documents:
        save_chunks(documents)
        print(f"\nCreated {len(documents)} chunks.")
        print("Saved to chunks.json")
    else:
        print("\nNo chunks created or saved.")

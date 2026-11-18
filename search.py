
from ddgs import DDGS
from urllib.parse import urlparse
import json


def search_web(question, max_results=6):
    """
    Search the web and return structured results.

    Args:
        question: User's search query.
        max_results: Maximum number of results.

    Returns:
        List of dictionaries containing
        title, url, and snippet.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    results = []
    seen_urls = set()

    try:
        with DDGS(timeout=15) as ddgs:
            raw_results = ddgs.text(
                query=question,
                max_results=max_results
            )

            for result in raw_results:
                title = result.get("title", "").strip()
                url = result.get("href", "").strip()
                snippet = result.get("body", "").strip()

                parsed = urlparse(url)

                # Only accept normal web links.
                if parsed.scheme not in ("http", "https"):
                    continue

                # Avoid duplicate sources.
                if url in seen_urls:
                    continue

                seen_urls.add(url)

                results.append({
                    "title": title,
                    "url": url,
                    "snippet": snippet
                })

    except Exception as error:
        print(f"Search failed: {error}")
        return []

    return results


def display_results(results):
    """Print search results to the terminal."""

    if not results:
        print("No results found.")
        return

    for index, result in enumerate(results, start=1):
        print(f"\n--- Result {index} ---")
        print("Title:", result["title"])
        print("URL:", result["url"])
        print("Snippet:", result["snippet"])


def save_results(results, filename="search_results.json"):
    """Save results to a JSON file."""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    question = input("Enter your research question: ")

    results = search_web(question)

    display_results(results)
    save_results(results)

    print("\nResults saved to search_results.json")
    
from datetime import datetime
import time
from ddgs import DDGS
from urllib.parse import urlparse
import json

def search_web(question, max_results=6, max_attempts=3):
    """
    Search DuckDuckGo with retry handling.
    """

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    for attempt in range(1, max_attempts + 1):
        try:
            results = []
            seen_urls = set()

            with DDGS(timeout=20) as ddgs:
                raw_results = ddgs.text(
                    query=question,
                    max_results=max_results,
                    backend="bing"
                )

                for result in raw_results:
                    title = result.get("title", "").strip()
                    url = result.get("href", "").strip()
                    snippet = result.get("body", "").strip()

                    parsed = urlparse(url)

                    if parsed.scheme not in ("http", "https"):
                        continue

                    if url in seen_urls:
                        continue

                    seen_urls.add(url)

                    results.append({
                        "title": title,
                        "url": url,
                        "snippet": snippet
                    })

            return results

        except Exception as error:
            print(
                f"Search attempt {attempt}/{max_attempts} "
                f"failed: {error}"
            )

            if attempt < max_attempts:
                wait_time = 2 ** attempt
                print(f"Waiting {wait_time} seconds...")
                time.sleep(wait_time)

    print("All search attempts failed.")
    return []


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



def save_results(results, filename=None):
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"search_results_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    print(f"\nResults saved to {filename}")

if __name__ == "__main__":
    question = input("Enter your research question: ")

    results = search_web(question)

    display_results(results)

    if results:
        save_results(results)
    else:
        print("\nNo results saved.")

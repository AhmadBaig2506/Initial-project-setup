
import pytest
from search import search_web


def test_empty_question():
    with pytest.raises(ValueError):
        search_web("")


def test_whitespace_question():
    with pytest.raises(ValueError):
        search_web("   ")


def test_search_result_structure():
    results = search_web(
        "What is machine learning?",
        max_results=3
    )

    # Live search may temporarily return no results.
    if not results:
        pytest.skip("Search provider unavailable")

    for result in results:
        assert "title" in result
        assert "url" in result
        assert "snippet" in result

        assert result["url"].startswith(
            ("http://", "https://")
        )

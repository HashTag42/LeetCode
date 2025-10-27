from mergeAlternately import Solution
import pytest


cases = [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
]


@pytest.mark.parametrize("word1, word2, expected", cases)
def test__mergeAlternately(word1, word2, expected):
    solution = Solution()
    assert solution.mergeAlternately(word1, word2) == expected

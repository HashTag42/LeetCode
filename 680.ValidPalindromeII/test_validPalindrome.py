from validPalindrome import Solution
import pytest


cases = [
    ("", True),
    ("aba", True),
    ("abca", True),
    ("caba", True),
    ("abac", True),
    ("abc", False),
]


@pytest.mark.parametrize("string, expected", cases)
def test__validPalindrome__(string, expected):
    solution = Solution()
    assert expected == solution.validPalindrome(string)

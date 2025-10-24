from validPalindrome import Solution
import pytest


cases = [
    ("aba", True),
    ("abca", True),
    ("abc", False),
]


@pytest.mark.parametrize("string, expected", cases)
def test__validPalindrome__(string, expected):
    solution = Solution()
    assert expected == solution.validPalindrome(string)

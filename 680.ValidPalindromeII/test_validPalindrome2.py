from validPalindrome2 import Solution
import pytest


validPalindrome2_cases = [
    ("", True),
    ("aba", True),
    ("abca", True),
    ("caba", True),
    ("abac", True),
    ("abc", False),
]


@pytest.mark.parametrize("string, expected", validPalindrome2_cases)
def test__validPalindrome2__(string, expected):
    solution = Solution()
    assert expected == solution.validPalindrome2(string)

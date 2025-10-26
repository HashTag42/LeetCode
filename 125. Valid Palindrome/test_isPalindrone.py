from isPalindrome import Solution
import pytest


cases = [
    ("", True),
    (" ", True),
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("0P", False),
]


@pytest.mark.parametrize("s, expected", cases)
def test__isPalindrome__(s, expected):
    solution = Solution()
    assert solution.isPalindrome(s) == expected

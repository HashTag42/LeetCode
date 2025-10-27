from isPalindrome import Solution
import pytest


cases = [
    ("", True),
    (" ", True),
    ("a", True),
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("0P", False),
    ("abba", True),
    ("abcba", True),
    ("abcabc", False),
]


@pytest.mark.parametrize("s, expected", cases)
def test__isPalindrome1__(s, expected):
    solution = Solution()
    assert solution.isPalindrome1(s) == expected


@pytest.mark.parametrize("s, expected", cases)
def test__isPalindrome2__(s, expected):
    solution = Solution()
    assert solution.isPalindrome2(s) == expected


@pytest.mark.parametrize("s, expected", cases)
def test__isPalindrome3__(s, expected):
    solution = Solution()
    assert solution.isPalindrome3(s) == expected

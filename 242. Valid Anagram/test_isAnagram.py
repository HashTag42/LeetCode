from isAnagram import Solution
import pytest


cases = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
]


@pytest.mark.parametrize("s, t, expected", cases)
def test__isAnagram__(s, t, expected):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected

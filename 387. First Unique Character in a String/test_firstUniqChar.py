from firstUniqChar import Solution
import pytest


cases = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
]


@pytest.mark.parametrize("s, expected", cases)
def test_Solution_firstUniqChar(s, expected):
    assert Solution().firstUniqChar(s) == expected

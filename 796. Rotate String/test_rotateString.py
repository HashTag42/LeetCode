from rotateString import Solution
import pytest


cases = [
    # s, goal, expected
    ("abcde", "cdeab", True),
    ("abcde", "abced", False),
]


@pytest.mark.parametrize("s, goal, expected", cases)
def test_Solution_rotateString(s, goal, expected):
    solution = Solution()
    assert solution.rotateString(s, goal) == expected

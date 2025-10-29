from isPowerOfTwo import Solution
import pytest


cases = [
    # n, expected
    (0, False),
    (1, True),
    (3, False),
    (8, True),
    (16, True),
]


@pytest.mark.parametrize("n, expected", cases)
def test_Solution_isPowerOfTwo(n, expected):
    assert Solution().isPowerOfTwo(n) == expected

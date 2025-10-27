from myPow import Solution
import pytest


cases = [
    (2.00000, 10, 1024),
    (2.10000, 3, 9.26100),
    (2.00000, -2, 0.25000),
    (0.44528, 0, 1),
    (7, 3, 343.000000),
    (4.73, 12, 125410439.217423),
    # (0.00001, 2147483647, 0),
]


@pytest.mark.parametrize("x, n, expected", cases)
def test__myPow__(x, n, expected):
    solution = Solution()
    assert pytest.approx(solution.myPow(x, n)) == expected

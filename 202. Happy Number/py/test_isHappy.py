from isHappy import Solution
import pytest


isHappy_cases = [
    (19, True),
    (2, False),
]


@pytest.mark.parametrize("n, expected", isHappy_cases)
def test__isHappy__(n, expected):
    solution = Solution()
    assert solution.isHappy(n) == expected


from isHappy import Solution
import pytest


isHappy_cases = [
    (19, True),
    (2, False),
]


squareDigits_cases = [
    (19, 82),
    (82, 68),
    (68, 100),
    (100, 1),
    (4, 16),
    (16, 37),
    (37, 58),
    (58, 89),
    (89, 145),
    (145, 42),
    (42, 20),
    (20, 4),
]


@pytest.mark.parametrize("n, expected", isHappy_cases)
def test__isHappy__(n, expected):
    solution = Solution()
    assert solution.isHappy(n) == expected


@pytest.mark.parametrize("n, expected", squareDigits_cases)
def test__squareDigits__(n, expected):
    solution = Solution()
    assert solution.squareDigits(n) == expected

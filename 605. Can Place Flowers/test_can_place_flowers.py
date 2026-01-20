from can_place_flowers import can_place_flowers
import pytest

can_place_flowers_test_cases = [
    # Basic examples from problem
    ([1, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 1], 2, False),

    # Edge cases: single element
    ([0], 1, True),
    ([0], 0, True),
    ([1], 0, True),
    ([1], 1, False),

    # Edge cases: two elements
    ([0, 0], 1, True),
    ([0, 0], 2, False),
    ([0, 1], 1, False),
    ([1, 0], 1, False),

    # Planting at edges
    ([0, 0, 1], 1, True),
    ([1, 0, 0], 1, True),
    ([0, 0, 0], 2, True),
    ([0, 0, 0], 1, True),

    # All empty
    ([0, 0, 0, 0, 0], 3, True),
    ([0, 0, 0, 0, 0], 2, True),
    ([0, 0, 0, 0, 0], 4, False),

    # All planted
    ([1, 0, 1, 0, 1], 0, True),
    ([1, 0, 1, 0, 1], 1, False),

    # n = 0 (always true)
    ([1, 1, 1], 0, True),  # invalid input per constraints, but n=0 should still work
    ([0, 0, 0], 0, True),

    # Longer sequences
    ([1, 0, 0, 0, 0, 1], 1, True),
    ([1, 0, 0, 0, 0, 1], 2, False),
    ([0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 3, True),
]


@pytest.mark.parametrize('flowerbed, n, expected', can_place_flowers_test_cases)
def test_can_place_flowers(flowerbed, n, expected):
    assert can_place_flowers(flowerbed.copy(), n) == expected

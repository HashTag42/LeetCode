from contains_nearby_duplicate import contains_nearby_duplicate
import pytest

test_cases = [
    ([1, 2, 3, 1], 3, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 3, 1, 2, 3], 2, False)
]


@pytest.mark.parametrize('nums, k, expected', test_cases)
def test_contains_nearby_duplicate(nums, k, expected):
    assert contains_nearby_duplicate(nums, k) == expected

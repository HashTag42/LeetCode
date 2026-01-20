from kids_with_candies import kids_with_candies
import pytest

test_cases = [
    # candies, extra_candies, expected
    ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
    ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
    ([12, 1, 12], 10, [True, False, True]),
]


@pytest.mark.parametrize('candies, extra_candies, expected', test_cases)
def test_kids_with_candies(candies, extra_candies, expected):
    assert kids_with_candies(candies, extra_candies) == expected

from largest_altitude import largest_altitude
import pytest


test_cases = [
    # (gain, expected)
    ([-5, 1, 5, 0, -7], 1),
    ([-4, -3, -2, -1, 4, 3, 2], 0),
]


@pytest.mark.parametrize('gain, expected', test_cases)
def test_largest_altitude(gain, expected):
    assert largest_altitude(gain) == expected

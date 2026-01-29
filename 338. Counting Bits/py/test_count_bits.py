import pytest
from count_bits import count_bits

test_cases = [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
]


@pytest.mark.parametrize('n, expected', test_cases)
def test_count_bits(n, expected):
    assert count_bits(n) == expected

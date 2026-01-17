from add_binary import add_binary
import pytest

add_binary_test_cases = [
    # a, b, expected
    ('11', '1', '100'),
    ('1010', '1011', '10101'),
]


@pytest.mark.parametrize('a, b, expected', add_binary_test_cases)
def test_add_binary(a, b, expected):
    assert add_binary(a, b) == expected

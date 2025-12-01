from reverse_string import reverse_string
import pytest

test_cases = [
    ([None], [None]),
    ([], []),
    (["a"], ["a"]),
    (["a", "b"], ["b", "a"]),
    (["a", "b", "c"], ["c", "b", "a"]),
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
]


@pytest.mark.parametrize("string, expected", test_cases)
def test_reverse_string(string, expected):
    reverse_string(string)
    assert string == expected

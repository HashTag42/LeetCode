from remove_duplicates import remove_duplicates
import pytest

test_cases = [
    # s, expected
    ('', ''),
    ('a', 'a'),
    ('ab', 'ab'),
    ('aa', ''),
    ('abbaca', 'ca'),
    ('azxxzy', 'ay'),
    ('aababaab', 'ba'),
]


@pytest.mark.parametrize('s, expected', test_cases)
def test_remove_duplicates(s, expected):
    assert remove_duplicates(s) == expected

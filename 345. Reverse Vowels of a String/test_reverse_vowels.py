from reverse_vowels import reverse_vowels
import pytest

test_cases = [
    # (s, expected)
    ('IceCreAm', 'AceCreIm'),
    ('leetcode', 'leotcede'),
]


@pytest.mark.parametrize('s, expected', test_cases)
def test_reverse_vowels(s, expected):
    assert reverse_vowels(s) == expected

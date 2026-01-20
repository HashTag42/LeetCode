from gcd_of_strings import gcd_of_strings
import pytest

test_cases = [
    # str1, str2, expected
    ('ABCABC', 'ABC', 'ABC'),
    ('ABABAB', 'ABAB', 'AB'),
    ('LEET', 'CODE', ''),
    ('AAAAAB', 'AAA', ''),
]


@pytest.mark.parametrize('str1, str2, expected', test_cases)
def test_gcd_of_strings(str1, str2, expected):
    assert gcd_of_strings(str1, str2) == expected

from is_subsequence import Solution
import pytest


test_cases = [
    # (s, t, expected)
    ('abc', 'ahbgdc', True),
    ('axc', 'ahbgdc', False),
    ('ace', 'abcde', True),
    ('aec', 'abcde', False),
]


@pytest.mark.parametrize('s, t, expected', test_cases)
def test_is_subsequence(s, t, expected):
    assert Solution().is_subsequence(s, t) == expected

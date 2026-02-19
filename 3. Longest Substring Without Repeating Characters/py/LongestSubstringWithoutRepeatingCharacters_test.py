import json
import pathlib
import pytest
from LongestSubstringWithoutRepeatingCharacters import Solution

root = pathlib.Path(__file__).resolve().parents[1]

lengthOfLongestSubstring_test_cases_path = root / "test_cases.json"

with open(lengthOfLongestSubstring_test_cases_path) as f:
    lengthOfLongestSubstring_test_cases = json.load(f)


@pytest.mark.parametrize('substring, expected', lengthOfLongestSubstring_test_cases)
def test_lengthOfLongestSubstring(substring, expected):
    sol = Solution()
    assert sol.lengthOfLongestSubstring(substring) == expected

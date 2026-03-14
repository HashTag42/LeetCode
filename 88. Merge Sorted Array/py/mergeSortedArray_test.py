import json
import pathlib
import pytest
from mergeSortedArray import Solution

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"
with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('nums1, m, nums2, n, expected', test_cases)
def test_mergeSortedArray(nums1, m, nums2, n, expected):
    assert Solution().mergeSortedArray(nums1, m, nums2, n) == expected

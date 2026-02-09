import json
import pathlib
import pytest
from AddTwoNumbers import Solution

root = pathlib.Path(__file__).resolve().parents[1]

addTwoNumbers_test_cases_path = root / "addTwoNumbers_tests.json"

with open(addTwoNumbers_test_cases_path) as f:
    addTwoNumbers_test_cases = json.load(f)


@pytest.mark.parametrize('l1, l2, expected', addTwoNumbers_test_cases)
def test_AddTwoNumbers(l1, l2, expected):
    sol = Solution()
    assert sol.addTwoNumbers(l1, l2) == expected


int_to_list_test_cases_path = root / "int_to_list_tests.json"

with open(int_to_list_test_cases_path) as f:
    int_to_list_test_cases = json.load(f)


@pytest.mark.parametrize('num, expected', int_to_list_test_cases)
def test_int_to_list(num, expected):
    sol = Solution()
    assert sol.int_to_list(num) == expected


list_to_int_test_cases_path = root / "list_to_int_tests.json"

with open(list_to_int_test_cases_path) as f:
    list_to_int_test_cases = json.load(f)


@pytest.mark.parametrize('l1, expected', list_to_int_test_cases)
def test_list_to_int(l1, expected):
    sol = Solution()
    assert sol.list_to_int(l1) == expected

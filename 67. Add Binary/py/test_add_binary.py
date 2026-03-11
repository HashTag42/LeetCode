import json
import pathlib
import pytest
from add_binary import add_binary

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"
with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('a, b, expected', test_cases)
def test_add_binary(a, b, expected):
    assert add_binary(a, b) == expected

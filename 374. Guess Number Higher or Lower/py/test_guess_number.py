import json
import pathlib
import pytest
from guess_number import guess_number

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"

with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('n, pick', test_cases)
def test_guess_number(n, pick):
    assert guess_number(n, pick) == pick

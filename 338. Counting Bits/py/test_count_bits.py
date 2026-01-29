import json
import pathlib
import pytest
from count_bits import count_bits

root = pathlib.Path(__file__).resolve().parents[1]
test_cases_path = root / "test_cases.json"

with open(test_cases_path) as f:
    test_cases = json.load(f)


@pytest.mark.parametrize('n, expected', test_cases)
def test_count_bits(n, expected):
    assert count_bits(n) == expected

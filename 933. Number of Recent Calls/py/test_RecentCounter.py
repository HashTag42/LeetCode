from RecentCounter import RecentCounter


def test_RecentCounter_example():
    inputs = [1, 100, 3001, 3002]
    expected = [1, 2, 3, 3]

    rc = RecentCounter()
    result = [rc.ping(t) for t in inputs]

    assert result == expected

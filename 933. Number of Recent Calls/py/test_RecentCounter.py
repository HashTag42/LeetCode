from RecentCounter import RecentCounter

input_a = ["RecentCounter", "ping", "ping", "ping", "ping"]
input_b = [[], [1], [100], [3001], [3002]]
expected = [None, 1, 2, 3, 3]


def test_RecentCounter():
    rc = RecentCounter()
    result = []
    for i, a in enumerate(input_a):
        match a:
            case "RecentCounter":
                result.append(None)
            case "ping":
                result.append(rc.ping(input_b[i][0]))
    assert result == expected

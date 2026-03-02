using System.Text.Json;
using Shared;
using Xunit;

namespace LeetCode.MergeTwoSortedLists;

public class MergeTwoSortedListsTests
{
    [Fact]
    public void TestCases_LoadsSuccessfully()
    {
        Assert.NotEmpty(TestCases);
    }

	public static TheoryData<int[]?, int[]?, int[]?> TestCases
	{
		get
		{
			var data = new TheoryData<int[]?, int[]?, int[]?>();
			var rows = TestDataLoader.LoadNestedArrayData("test_cases.json");
			foreach (var row in rows)
			{
				var list1 = row[0] is JsonElement list1El
					? list1El.EnumerateArray().Select(e => e.GetInt32()).ToArray()
					: null;
				var list2 = row[1] is JsonElement list2El
					? list2El.EnumerateArray().Select(e => e.GetInt32()).ToArray()
					: null;
				var expected = row[2] is JsonElement expectedEl
					? expectedEl.EnumerateArray().Select(e => e.GetInt32()).ToArray()
					: null;
				data.Add(list1, list2, expected);
			}
			return data;
		}
	}

	[Theory]
	[MemberData(nameof(TestCases))]
	public void TestMergeTwoLists(int[]? list1, int[]? list2, int[]? expected)
	{
		var l1 = ToLinkedList(list1);
		var l2 = ToLinkedList(list2);

		var merged = Solution.MergeTwoLists(l1, l2);

		Assert.Equal(expected, ToArray(merged));
	}

	private static ListNode? ToLinkedList(int[]? values)
	{
		if (values == null || values.Length == 0)
		{
			return null;
		}

		var dummy = new ListNode();
		var current = dummy;
		foreach (var value in values)
		{
			current.next = new ListNode(value);
			current = current.next;
		}

		return dummy.next;
	}

	private static int[]? ToArray(ListNode? head)
	{
		if (head == null)
		{
			return null;
		}

		var values = new List<int>();
		var current = head;
		while (current != null)
		{
			values.Add(current.val);
			current = current.next;
		}

		return [.. values];
	}
}

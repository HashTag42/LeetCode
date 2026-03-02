// LeetCode problem: 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/description/

namespace LeetCode.MergeTwoSortedLists;

// Definition for singly-linked list.
public class ListNode
{
    public int val;
    public ListNode? next;
    public ListNode(int val = 0, ListNode? next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution
{
    public static ListNode? MergeTwoLists(ListNode? list1, ListNode? list2)
    {
        // Create a dummy node to simplify logic
        ListNode dummy = new(0);
        ListNode current = dummy;

        // Merge by comparing nodes and attaching the smaller one
        while (list1 != null && list2 != null)
        {
            if (list1.val <= list2.val)
            {
                current.next = list1;
                list1 = list1.next;
            }
            else
            {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }

        // Attach remaining nodes
        current.next = list1 ?? list2;

        return dummy.next;
    }
}
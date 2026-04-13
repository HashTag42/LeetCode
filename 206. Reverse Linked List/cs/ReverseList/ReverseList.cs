/*
LeetCode Problem 206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
*/

namespace LeetCode.ReverseList;

 public class ListNode(int val = 0, ListNode? next = null)
{
    public int val = val;
    public ListNode? next = next;
}

public class Solution
{
    public ListNode? ReverseList(ListNode? head)
    {
        ListNode? prev = null;
        ListNode? current = head;
        while (current != null)
        {
            ListNode? nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }
        return prev;
    }
}
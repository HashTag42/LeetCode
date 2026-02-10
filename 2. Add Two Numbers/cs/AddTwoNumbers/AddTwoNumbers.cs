/*
LeetCode Problem 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/
*/

// Definition for singly-linked list.
// public class ListNode {
//     public int val;
//     public ListNode next;
//     public ListNode(int val=0, ListNode next=null) {
//         this.val = val;
//         this.next = next;
//     }
// }

namespace LeetCode.AddTwoNumbers;

public class Solution
{
    public static int[] AddTwoNumbers(int[]? list1, int[]? list2)
    {
        return IntToList(ListToInt(list1) + ListToInt(list2));
    }

    private static long ListToInt(int[]? list)
    {
        if (list is null) return 0;
        long number = 0;
        for (int n = 0; n < list.Length; n++)
        {
            number += list[n] * (long)Math.Pow(10, n);
        }
        return number;
    }

    private static int[] IntToList(long num)
    {
        string sNum = num.ToString();
        int lenS = sNum.Length;
        int[] result = new int[lenS];
        for (int i = 0; i < lenS; i++)
        {
            result[i] = int.Parse(sNum[lenS - i - 1].ToString());
        }
        return result;
    }
}
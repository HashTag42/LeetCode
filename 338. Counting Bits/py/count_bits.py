'''
LeetCode problem 338. Counting Bits
https://leetcode.com/problems/counting-bits/description/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's
in the binary representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10

Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101
'''
from collections import Counter


def count_bits(n: int) -> list[int]:
    '''
    Complexity:
        Time: O(n log n)
        Space: O(n)
    '''
    result: list[int] = []
    for i in range(0, n + 1):
        b = bin(i)
        c = Counter(b)
        result.append(c['1'])
    return result

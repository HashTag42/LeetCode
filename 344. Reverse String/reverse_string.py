'''
LeetCode problem 344. Reverse String
https://leetcode.com/problems/reverse-string/description

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.
'''
from typing import List


def reverse_string(s: List[str]) -> List[str]:
    length = len(s)
    for i in range(length // 2):
        temp = s[i]
        s[i] = s[length - i - 1]
        s[length - i - 1] = temp

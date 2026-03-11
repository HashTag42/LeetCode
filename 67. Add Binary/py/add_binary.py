'''
LeetCode problem 67. Add Binary
https://leetcode.com/problems/add-binary/description/

Given two binary strings a and b, return their sum as a binary string.
'''


def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]

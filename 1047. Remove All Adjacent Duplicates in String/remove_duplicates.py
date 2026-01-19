'''
LeetCode problem 1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

You are given a string `s` consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on `s` until we no longer can.
Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.
'''


def remove_duplicates(s: str) -> str:
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    if len(s) < 2:
        return s
    chars = [s[0]]
    i = 1
    while True:
        if len(chars) >= 1 and chars[-1] == s[i]:
            chars.pop()
        else:
            chars.append(s[i])
        i += 1
        if i == len(s):
            break
    return ''.join(chars)

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
    length = len(s)
    string = list(s)
    i = 0
    while True:
        if 1 < length and i < length - 1:
            if string[i] == string[i + 1]:
                # Remove both characters
                string.pop(i + 1)
                string.pop(i)
                length -= 2
                i = 0
            else:
                i += 1
        else:
            break
    return ''.join(string)

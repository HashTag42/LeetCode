'''
LeetCode problem 1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

You are given a string `s` consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on `s` until we no longer can.
Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.

test_cases = [
    # s, expected
    ('', ''),
    ('a', 'a'),
    ('ab', 'ab'),
    ('aa', ''),
    ('abbaca', 'ca'),
    ('azxxzy', 'ay'),
    ('aababaab', 'ba'),
]
'''


def remove_duplicates(s: str) -> str:
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    chars = []
    for ch in s:
        if chars and chars[-1] == ch:
            chars.pop()
        else:
            chars.append(ch)
    return ''.join(chars)

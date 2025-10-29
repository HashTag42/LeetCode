'''
LeetCode problem 387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = dict()
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        keys = [k for k, v in counter.items() if v == 1]

        return s.index(keys[0]) if len(keys) > 0 else -1

'''
LeetCode problem 1768. Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/
'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        if len(word1) <= len(word2):
            short_word, long_word = word1, word2
        else:
            short_word, long_word = word2, word1
        for i in range(len(short_word)):
            result += word1[i] + word2[i]
        result += long_word[len(short_word):]
        return result

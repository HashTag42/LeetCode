# LeetCode problem: 383. Ransom Note: <https://leetcode.com/problems/ransom-note/description/>


from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteLetters = defaultdict(str)
        magazineLetters = defaultdict(str)
        for letter in magazine:
            magazineLetters[letter] = magazineLetters.get(letter, 0) + 1
        for letter in ransomNote:
            ransomNoteLetters[letter] = ransomNoteLetters.get(letter, 0) + 1
            mval = magazineLetters.get(letter)
            if mval is None or mval < ransomNoteLetters.get(letter):
                return False
        return True

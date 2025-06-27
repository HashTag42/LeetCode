# LeetCode problem: 383. Ransom Note: <https://leetcode.com/problems/ransom-note/description/>

import unittest
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


class Solution_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Case1(self):
        self.assertEqual(self.solution.canConstruct("a", "b"), False)

    def test_Case2(self):
        self.assertEqual(self.solution.canConstruct("aa", "ab"), False)

    def test_Case3(self):
        self.assertEqual(self.solution.canConstruct("aa", "aab"), True)


if __name__ == "__main__":
    unittest.main()
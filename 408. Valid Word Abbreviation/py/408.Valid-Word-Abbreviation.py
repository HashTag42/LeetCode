# LeetCode problem 408. Valid Word Abbreviation
# https://leetcode.com/problems/valid-word-abbreviation/description/

import unittest


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_len = len(word)
        abbr_cnt = 0
        number = ""
        for a in abbr:
            if abbr_cnt >= word_len:
                # Expanded abbreviation can't be longer than the word
                return False
            if a.isdecimal():
                if number == "" and int(a) == 0:
                    # Leading zero
                    return False
                else:
                    number += a
            else:
                if number != "":
                    abbr_cnt += int(number)
                    number = ""
                    if abbr_cnt < word_len:
                        if a != word[abbr_cnt]:
                            # Out of sync
                            return False
                    abbr_cnt += 1
                else:
                    abbr_cnt += 1
        if number != "":
            abbr_cnt += int(number)
        return True if word_len == abbr_cnt else False


class Solution_validWordAbbreviation_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        return super().setUp()

    def test_validWordAbbreviation_Case_1(self):
        self.assertEqual(self.solution.validWordAbbreviation("internationalization", "i12iz4n"), True)

    def test_validWordAbbreviation_Case_2(self):
        self.assertEqual(self.solution.validWordAbbreviation("apple", "a2e"), False)

    def test_validWordAbbreviation_Case_3(self):
        self.assertEqual(self.solution.validWordAbbreviation("internationalization", "i5a11o1"), True)

    def test_validWordAbbreviation_Case_4(self):
        self.assertEqual(self.solution.validWordAbbreviation("hi", "hi1"), False)

    def test_validWordAbbreviation_Case_5(self):
        self.assertEqual(self.solution.validWordAbbreviation("word", "3e"), False)

    def test_validWordAbbreviation_Case_6(self):
        self.assertEqual(self.solution.validWordAbbreviation("hi", "2i"), False)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()

# LeetCode problem 408: Valid Word Abbreviation
# https://leetcode.com/problems/valid-word-abbreviation/description/

import unittest


class Solution:
    def validWordAbbreviation(seld, word: str, abbr: str) -> bool:
        """
        Checks if the abbreviation matches the given word.

        Args:
            word (str): The original word.
            abbr (str): The abbreviation to validate.

        Returns:
            bool: True if the abbreviation is valid, False otherwise.

        Rules:
            - Abbreviations may replace non-adjacent substrings with their lengths.
            - Leading zeros in numbers are invalid.
            - Empty substrings cannot be abbreviated.
        """
        word_len = len(word)
        abbr_cnt = 0    # Pointer to current position in word
        num_str = ""    # Accumulates digits to form a number
        for char in abbr:
            if char.isdigit():
                # Reject leading zero in abbreviation
                if num_str == "" and int(char) == 0:
                    return False
                num_str += char
            else:
                # If there's a pending number, skip that many characters
                if num_str:
                    abbr_cnt += int(num_str)
                    num_str = ""
                # Check if current character matches the word
                if abbr_cnt < word_len and char != word[abbr_cnt]:
                    return False
                abbr_cnt += 1

        # Handle any remaining number of the end of abbreviation
        if num_str != "":
            abbr_cnt += int(num_str)

        return word_len == abbr_cnt


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

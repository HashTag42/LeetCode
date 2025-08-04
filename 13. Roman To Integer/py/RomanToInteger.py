# LeetCode challenge: 13. Roman to Integer
# <https://leetcode.com/problems/roman-to-integer/description/>

import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while (True):
            if i == len(s):
                break
            c = s[i]
            n = s[i+1] if (i < len(s) - 1) else ""
            if (
                ((c == "I") and (n == "V" or n == "X"))
                or ((c == "X") and (n == "L" or n == "C"))
                or ((c == "C") and (n == "D" or n == "M"))
            ):
                c += n
                i += 1
            total += self.roman_value(c)
            i += 1

        return total

    def roman_value(self, s: str) -> int:
        match s:
            case "I": return 1
            case "IV": return 4
            case "V": return 5
            case "IX": return 9
            case "X": return 10
            case "XL": return 40
            case "L": return 50
            case "XC": return 90
            case "C": return 100
            case "CD": return 400
            case "D": return 500
            case "CM": return 900
            case "M": return 1000
            case _: raise ValueError("Unsupported value")


class romanToInt_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_III_3(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)

    def test_XII_12(self):
        self.assertEqual(self.solution.romanToInt("XII"), 12)

    def test_XXVII_27(self):
        self.assertEqual(self.solution.romanToInt("XXVII"), 27)

    def test_LVIII_58(self):
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)

    def test_IV_4(self):
        self.assertEqual(self.solution.romanToInt("IV"), 4)

    def test_IX_9(self):
        self.assertEqual(self.solution.romanToInt("IV"), 4)

    def test_XL_40(self):
        self.assertEqual(self.solution.romanToInt("XL"), 40)

    def test_XC_90(self):
        self.assertEqual(self.solution.romanToInt("XC"), 90)

    def test_CD_400(self):
        self.assertEqual(self.solution.romanToInt("CD"), 400)

    def test_CM_900(self):
        self.assertEqual(self.solution.romanToInt("CM"), 900)


class roman_value_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_Values(self):
        self.assertEqual(self.solution.roman_value("I"),    1)
        self.assertEqual(self.solution.roman_value("IV"),   4)
        self.assertEqual(self.solution.roman_value("V"),    5)
        self.assertEqual(self.solution.roman_value("IX"),   9)
        self.assertEqual(self.solution.roman_value("X"),   10)
        self.assertEqual(self.solution.roman_value("XL"),  40)
        self.assertEqual(self.solution.roman_value("L"),   50)
        self.assertEqual(self.solution.roman_value("XC"),  90)
        self.assertEqual(self.solution.roman_value("C"),  100)
        self.assertEqual(self.solution.roman_value("CD"), 400)
        self.assertEqual(self.solution.roman_value("D"),  500)
        self.assertEqual(self.solution.roman_value("CM"), 900)
        self.assertEqual(self.solution.roman_value("M"), 1000)

    def test_ValueError(self):
        with self.assertRaises(ValueError):
            self.solution.roman_value("")


if __name__ == "__main__":
    unittest.main()

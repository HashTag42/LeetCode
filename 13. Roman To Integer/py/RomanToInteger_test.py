import unittest
from RomanToInteger import Solution


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

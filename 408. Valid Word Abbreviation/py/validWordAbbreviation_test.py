import unittest
from validWordAbbreviation import Solution


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

    def test_validWordAbbreviation_Case_7(self):
        self.assertEqual(self.solution.validWordAbbreviation("hi", "02i"), False)

    def tearDown(self):
        return super().tearDown()

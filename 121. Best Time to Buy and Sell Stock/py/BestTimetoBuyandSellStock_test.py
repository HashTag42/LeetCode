import unittest
from BestTimetoBuyandSellStock import Solution


class maxProfit_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test01(self):
        self.assertEqual(self.solution.maxProfit([0]), 0)

    def test02(self):
        self.assertEqual(self.solution.maxProfit([0, 0]), 0)

    def test03(self):
        self.assertEqual(self.solution.maxProfit([0, 1]), 1)

    def test04(self):
        self.assertEqual(self.solution.maxProfit([1, 0]), 0)

    def test05(self):
        self.assertEqual(self.solution.maxProfit([0, 1, 2]), 2)

    def test06(self):
        self.assertEqual(self.solution.maxProfit([0, 2, 1]), 2)

    def test07(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test08(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test09(self):
        self.assertEqual(self.solution.maxProfit([0, 2, 1, 4]), 4)

    def test10(self):
        self.assertEqual(self.solution.maxProfit([0, 1, 2, 3, 4, 5]), 5)

    def test11(self):
        self.assertEqual(self.solution.maxProfit([2, 4, 1, 4]), 3)

    def test12(self):
        self.assertEqual(self.solution.maxProfit([2, 4, 1]), 2)

    def test13(self):
        self.assertEqual(self.solution.maxProfit([2, 5, 1, 3]), 3)

    def test14(self):
        self.assertEqual(self.solution.maxProfit([3, 2, 6, 5, 0, 3]), 4)

    def tearDown(self):
        pass

import unittest
from PascalTriangle import Solution


class Generate_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test01(self):
        self.assertEqual(self.solution.generate(0), [])

    def test02(self):
        self.assertEqual(self.solution.generate(1), [[1]])

    def test03(self):
        self.assertEqual(self.solution.generate(2), [[1], [1, 1]])

    def test04(self):
        self.assertEqual(self.solution.generate(3), [[1], [1, 1], [1, 2, 1]])

    def test05(self):
        self.assertEqual(self.solution.generate(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

import unittest
from FindTheTownJudge import Solution


class findJudge_Tests(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1(self):
        self.assertEqual(self.sol.findJudge(2, [[1, 2]]), 2)

    def test_2(self):
        self.assertEqual(self.sol.findJudge(3, [[1, 3], [2, 3]]), 3)

    def test_3(self):
        self.assertEqual(self.sol.findJudge(3, [[1, 3], [2, 3], [3, 1]]), -1)

    def test_4(self):
        self.assertEqual(self.sol.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]), 3)

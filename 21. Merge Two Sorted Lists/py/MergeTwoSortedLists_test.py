import unittest
from MergeTwoSortedLists import Solution


class mergeTwoLists_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mergeTwoLists_example_1(self):
        self.assertEqual(self.solution.mergeTwoLists([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4])

    def test_mergeTwoLists_example_2(self):
        self.assertEqual(self.solution.mergeTwoLists([], []), [])

    def test_mergeTwoLists_example_3(self):
        self.assertEqual(self.solution.mergeTwoLists([], [0]), [0])

    def test_mergeTwoLists_example_4(self):
        self.assertEqual(self.solution.mergeTwoLists([0], []), [0])

    def test_mergeTwoLists_example_5(self):
        self.assertEqual(self.solution.mergeTwoLists(None, None), None)

    def test_mergeTwoLists_example_6(self):
        self.assertEqual(self.solution.mergeTwoLists(None, [1]), [1])

    def test_mergeTwoLists_example_7(self):
        self.assertEqual(self.solution.mergeTwoLists([1], None), [1])

    def test_mergeTwoLists_example_11(self):
        self.assertEqual(self.solution.mergeTwoLists([0], [0]), [0, 0])

    def test_mergeTwoLists_example_12(self):
        self.assertEqual(self.solution.mergeTwoLists([0], [1]), [0, 1])

    def test_mergeTwoLists_example_13(self):
        self.assertEqual(self.solution.mergeTwoLists([1], [0]), [0, 1])

    def test_mergeTwoLists_example_14(self):
        self.assertEqual(self.solution.mergeTwoLists([0], [1, 2]), [0, 1, 2])

    def test_mergeTwoLists_example_15(self):
        self.assertEqual(self.solution.mergeTwoLists([1], [0, 2]), [0, 1, 2])

    def test_mergeTwoLists_example_16(self):
        self.assertEqual(self.solution.mergeTwoLists([2], [0, 1]), [0, 1, 2])

    def test_mergeTwoLists_example_17(self):
        self.assertEqual(self.solution.mergeTwoLists([1, 2], [0]), [0, 1, 2])

    def test_mergeTwoLists_example_18(self):
        self.assertEqual(self.solution.mergeTwoLists([0, 2], [1]), [0, 1, 2])

    def test_mergeTwoLists_example_19(self):
        self.assertEqual(self.solution.mergeTwoLists([0, 1], [2]), [0, 1, 2])

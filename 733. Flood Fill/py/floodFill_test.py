import unittest
from floodFill import Solution


class floodFill_Tests(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test01(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr,  sc,  color = 1,  1,  2
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test02(self):
        image = [[0, 0, 0], [0, 0, 0]]
        sr,  sc,  color = 0,  0,  0
        expected = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test03(self):
        image = [[0]]
        sr,  sc,  color = 0,  0,  0
        expected = [[0]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test04(self):
        image = [[0]]
        sr,  sc,  color = 0,  0,  2
        expected = [[2]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test05(self):
        image = [[1, 1], [1, 0]]
        sr,  sc,  color = 0,  0,  2
        expected = [[2, 2], [2, 0]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test06(self):
        image = [[1, 1], [0, 1]]
        sr,  sc,  color = 0,  0,  2
        expected = [[2, 2], [0, 2]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test07(self):
        image = [[1, 0], [1, 1]]
        sr,  sc,  color = 0,  0,  2
        expected = [[2, 0], [2, 2]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test08(self):
        image = [[0, 1], [1, 1]]
        sr,  sc,  color = 1,  1,  2
        expected = [[0, 2], [2, 2]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test09(self):
        image = [[0, 1], [1, 1]]
        sr,  sc,  color = 1,  0,  2
        expected = [[0, 2], [2, 2]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test10(self):
        image = [[0, 1], [1, 1]]
        sr,  sc,  color = 0,  1,  2
        expected = [[0, 2], [2, 2]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test11(self):
        image = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        sr,  sc,  color = 1,  1,  2
        expected = [[0, 2, 0], [2, 2, 2], [0, 2, 0]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test12(self):
        image = [[1, 1, 1]]
        sr,  sc,  color = 0,  0,  2
        expected = [[2, 2, 2]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test13(self):
        image = [[0, 1, 1]]
        sr,  sc,  color = 0,  1,  2
        expected = [[0, 2, 2]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def test14(self):
        image = [[1, 1, 1]]
        sr,  sc,  color = 0,  2,  2
        expected = [[2, 2, 2]]
        self.assertEqual(self.s.floodFill(image,  sr,  sc,  color),  expected)

    def tearDown(self):
        return super().tearDown()

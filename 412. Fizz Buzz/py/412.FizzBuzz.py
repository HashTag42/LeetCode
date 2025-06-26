# LeetCode challenge: 412. Fizz Buzz: <https://leetcode.com/problems/fizz-buzz/description/>

import unittest
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n+1):
            result = ""
            if i % 3 == 0:
                result = "Fizz"
            if i % 5 == 0:
                result += "Buzz"
            if result == "":
                result = f"{i}"
            output.append(result)
        return output
    
class Solution_fizzBuzz_Tests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_Case1(self):
        self.assertEqual(self.solution.fizzBuzz(3), ["1","2","Fizz"])
    def test_Case2(self):
        self.assertEqual(self.solution.fizzBuzz(5), ["1","2","Fizz","4","Buzz"])
    def test_Case3(self):
        self.assertEqual(self.solution.fizzBuzz(15), ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])

if __name__ == "__main__":
    unittest.main()
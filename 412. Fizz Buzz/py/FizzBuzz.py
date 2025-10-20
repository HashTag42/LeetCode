# LeetCode challenge: 412. Fizz Buzz: <https://leetcode.com/problems/fizz-buzz/description/>

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

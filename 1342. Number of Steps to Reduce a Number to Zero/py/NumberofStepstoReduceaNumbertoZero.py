# LeetCode challenge: 1342. Number of Steps to Reduce a Number to Zero:
# <https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/>

class Solution:
    # Time Complexity = O(logn)
    # Space Complexity = O(1)
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while (num > 0):
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
        return steps

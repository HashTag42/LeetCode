# LeetCode challenge: 997. Find the Town Judge
# <https://leetcode.com/problems/find-the-town-judge/description/>

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = -1

        trusting_people = {}
        trusted_people = {}
        for p in range(n):
            trusting_people[p+1] = 0
            trusted_people[p+1] = 0

        # Count how many times a person is trusted
        for t in trust:
            trusting_people[t[0]] += 1
            trusted_people[t[1]] += 1

        # Find the most trusted person
        max_key = None
        max_value = -1
        for key, value in trusted_people.items():
            if value >= max_value:
                max_value = value
                max_key = key

        if trusting_people[max_key] == 0 and max_value == n - 1:
            judge = max_key

        return judge

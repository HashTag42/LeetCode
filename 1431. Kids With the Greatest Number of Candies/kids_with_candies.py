'''
LeetCode problem 1431. Kids With the Greatest Number of Candies
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

There are `n` kids with candies. You are given an integer array `candies`,
where each `candies[i]` represents the number of candies the `ith` kid has,
and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `true` if,
after giving the `ith` kid all the `extraCandies`, they will have the greatest number
of candies among all the kids, or `false` otherwise.

Note that multiple kids can have the greatest number of candies.

Examples:
    # candies, extra_candies, expected
    ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
    ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
    ([12, 1, 12], 10, [True, False, True]),

Constraints:
    * `n == candies.length`
    * `2 <= n <= 100`
    * `1 <= candies[i] <= 100`
    * `1 <= extraCandies <= 50`
'''


def kids_with_candies(candies: list[int], extra_candies: int) -> list[bool]:
    '''
    Return a boolean array `result` of length `n`, where `result[i]` is `true` if,
    after giving the `ith` kid all the `extraCandies`, they will have the greatest number
    of candies among all the kids, or `false` otherwise.

    Time complexity: O(n)
    Space complexity: O(1)
    '''
    max_candies = max(candies)
    return [candy + extra_candies >= max_candies for candy in candies]

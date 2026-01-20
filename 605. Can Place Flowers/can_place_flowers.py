'''
LeetCode problem 605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1`
means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the
`flowerbed` without violating the no-adjacent-flowers rule and `false` otherwise.

Example 1:
    Input: `flowerbed = [1,0,0,0,1], n = 1`
    Output: `true`

Example 2:
    Input: `flowerbed = [1,0,0,0,1], n = 2`
    Output: `false`

Constraints:
    `1 <= flowerbed.length <= 2 * 10^4`
    `flowerbed[i]` is `0` or `1`.
    There are no two adjacent flowers in `flowerbed`.
    `0 <= n <= flowerbed.length`
'''


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    '''
    Determine if `n` flowers can be planted without adjacent flowers.

    Uses a greedy approach: plant at each valid position from left to right.
    Modifies the input array in place.

    Time complexity: O(n)
    Space complexity: O(1)
    '''
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            if left_empty and right_empty:
                flowerbed[i] = 1  # plant here
                count += 1
                if count >= n:  # early exit
                    return True
    return count >= n

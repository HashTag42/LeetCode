'''
LeetCode problem 374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/description/

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the
game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

    -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:
    Input: n = 10, pick = 6
    Output: 6

Example 2:
    Input: n = 1, pick = 1
    Output: 1

Example 3:
    Input: n = 2, pick = 1
    Output: 1

Constraints:
    1 <= n <= 231 - 1
    1 <= pick <= n
'''


def guess_number(n: int, pick: int) -> int:
    bottom, top = 0, n
    num = n // 2
    while True:
        result = guess(num, pick)
        if result == 1:
            bottom = num
            delta = (top - num) // 2
            delta = 1 if delta == 0 else delta
            num += delta
        elif result == -1:
            top = num
            delta = (num - bottom) // 2
            delta = 1 if delta == 0 else delta
            num -= delta
        else:   # result == 0
            return num


def guess(num: int, pick: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:   # num == pick
        return 0

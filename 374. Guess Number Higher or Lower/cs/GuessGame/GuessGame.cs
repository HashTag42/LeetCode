/*
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
*/

namespace LeetCode.GuessGame;

public class GuessGame
{

    private readonly int pick;

    public GuessGame(int pick)
    {
        this.pick = pick;
    }

    public int GuessNumber(int n)
    {
        int bottom = 0;
        int top = n;
        int num = n / 2;
        while (true)
        {
            int result = guess(num);
            if (result == 1)
            {
                bottom = num;
                int delta = (top - num) / 2;
                delta = delta == 0 ? 1 : delta;
                num += delta;
            }
            else if (result == -1)
            {
                top = num;
                int delta = (num - bottom) / 2;
                delta = delta == 0 ? 1 : delta;
                num -= delta;
            }
            else    // result == 0
            {
                return num;
            }
        }
    }

    public int guess(int num)
    {
        if (num > pick)
            return -1;
        else if (num < this.pick)
            return 1;
        else
            return 0;
    }
}
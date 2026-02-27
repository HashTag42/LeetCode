// LeetCode problem: 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/description/

namespace LeetCode.ValidParentheses;

public class Solution
{
    public bool IsValid(string s)
    {
        var stack = new Stack<char>();
        var pairs = new Dictionary<char, char>
        {
            [')'] = '(',
            [']'] = '[',
            ['}'] = '{'
        };

        foreach (char c in s)
        {
            if (c is '(' or '[' or '{')
                stack.Push(c);
            else if (stack.Count == 0 || stack.Peek() != pairs[c])
                return false;
            else
                stack.Pop();
        }

        return s.Length > 0 && stack.Count == 0;
    }
}

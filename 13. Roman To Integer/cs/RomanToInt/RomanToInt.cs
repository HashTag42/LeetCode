// LeetCode problem: 13. Roman to Integer
// https://leetcode.com/problems/roman-to-integer/description/

namespace LeetCode.RomanToInt;

public class Solution
{
    public static int RomanToInt(string s)
    {
        int total = 0;
        int i = 0;
        while (i < s.Length)
        {
            string c = s.Substring(i, 1);
            string n = i < s.Length - 1 ? s[i + 1].ToString() : "";
            if ((c == "I" && (n == "V" || n == "X")) ||
                (c == "X" && (n == "L" || n == "C")) ||
                (c == "C" && (n == "D" || n == "M")))
            {
                c += n;
                i += 1;
            }
            total += RomanValue(c);
            i += 1;
        }
        return total;
    }

    public static int RomanValue(string s)
    {
        return s switch
        {
            "I" => 1,
            "IV" => 4,
            "V" => 5,
            "IX" => 9,
            "X" => 10,
            "XL" => 40,
            "L" => 50,
            "XC" => 90,
            "C" => 100,
            "CD" => 400,
            "D" => 500,
            "CM" => 900,
            "M" => 1000,
            _ => throw new ArgumentException($"Unsupported value: {s}", nameof(s)),
        };
    }
}

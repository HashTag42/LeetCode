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
        switch(s)
        {
            case "I":   return 1;
            case "IV":  return 4;
            case "V":   return 5;
            case "IX":  return 9;
            case "X":   return 10;
            case "XL":  return 40;
            case "L":   return 50;
            case "XC":  return 90;
            case "C":   return 100;
            case "CD":  return 400;
            case "D":   return 500;
            case "CM":  return 900;
            case "M":   return 1000;
            default: throw new ArgumentException($"Unsupported value: {s}", nameof(s));
        }
    }
}

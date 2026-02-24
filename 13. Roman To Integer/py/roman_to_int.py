# LeetCode challenge: 13. Roman to Integer
# <https://leetcode.com/problems/roman-to-integer/description/>

class Solution:
    def roman_to_int(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            c = s[i]
            n = s[i + 1] if i < len(s) - 1 else ""
            if (c == "I" and (n == "V" or n == "X")) or \
               (c == "X" and (n == "L" or n == "C")) or \
               (c == "C" and (n == "D" or n == "M")):
                c += n
                i += 1
            total += self.roman_value(c)
            i += 1
        return total

    def roman_value(self, s: str) -> int:
        match s:
            case "I": return 1
            case "IV": return 4
            case "V": return 5
            case "IX": return 9
            case "X": return 10
            case "XL": return 40
            case "L": return 50
            case "XC": return 90
            case "C": return 100
            case "CD": return 400
            case "D": return 500
            case "CM": return 900
            case "M": return 1000
            case _: raise ValueError("Unsupported value")

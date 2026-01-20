'''
LeetCode problem 1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/

For two strings `s` and `t`, we say "`t` divides `s`" if and only
if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x`
such that `x` divides both `str1` and `str2`.

Constraints:

* `1 <= str1.length, str2.length <= 1000`
* `str1` and `str2` consist of English uppercase letters.

test_cases = [
    # str1, str2, expected
    ('ABCABC', 'ABC', 'ABC'),
    ('ABABAB', 'ABAB', 'AB'),
    ('LEET', 'CODE', ''),
    ('AAAAAB', 'AAA', ''),
]
'''
from math import gcd


def gcd_of_strings(str1: str, str2: str) -> str:
    # If a common divisor exists, concatenation order doesn't matter
    if str1 + str2 != str2 + str1:
        return ''
    # The GCD string length equals GCD of the two lengths
    return str1[:gcd(len(str1), len(str2))]

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


def gcd_of_strings(str1: str, str2: str) -> str:
    '''
    Returns the largest string `x` such that `x` divides both `str1` and `str2`.

    Time complexity:
    Space complexity:
    '''
    x, current = '', ''
    for ch in str2:
        current += ch
        if divides_by(str1, current) and divides_by(str2, current):
            x = current
    return x


def divides_by(s1: str, s2: str) -> bool:
    if len(s1) % len(s2) != 0:
        return False
    times = len(s1) // len(s2)
    if times >= 2:
        repeat = s2
        for i in range(1, times):
            s2 += repeat
    if s1 == s2:
        return True
    return False

'''
LeetCode problem 345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
lower and upper cases, more than once.

Example 1:
    Input: s = "IceCreAm"
    Output: "AceCreIm"
    Explanation:
        The vowels in s are ['I', 'e', 'e', 'A'].
        On reversing the vowels, s becomes "AceCreIm".

Example 2:
    Input: s = "leetcode"
    Output: "leotcede"

Constraints:
    1 <= s.length <= 3 * 10^5
    s consist of printable ASCII characters.
'''

VOWELS: set[str] = set('aeiouAEIOU')


def reverse_vowels(s: str) -> str:
    '''
    Reverse all the vowels in a string.

    Time complexity: O(n)
    Space complexity: O(n)
    '''
    result = list(s)
    # Collect all the vowels and their indexes
    vowels: list[str] = []
    indexes: list[int] = []
    for i, v in enumerate(s):
        if v in VOWELS:
            vowels.append(v)
            indexes.append(i)

    # Reverse the vowels
    vowels.reverse()

    # Replace the vowels in s
    for idx, vowel in zip(indexes, vowels):
        result[idx] = vowel

    return ''.join(result)

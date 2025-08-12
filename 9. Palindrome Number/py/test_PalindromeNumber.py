import pytest
from PalindromeNumber import Solution

@pytest.fixture
def solution():
    return Solution()

class TestSolution:
    def test_PalindromeWithOddNumberOfDigits_IsTrue(self, solution):
        assert solution.isPalindrome(121) == True

    def test_PalindromeWithNegativeNumber_IsFalse(self, solution):
        assert solution.isPalindrome(-121) == False

    def test_PalindromeWithEvenNumberOfDigits_IsFalse(self, solution):
        assert solution.isPalindrome(10) == False

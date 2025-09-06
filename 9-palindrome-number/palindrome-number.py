class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        original = x

        while x > 0:
            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x //= 10

        return reverse == original
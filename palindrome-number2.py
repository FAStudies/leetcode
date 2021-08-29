class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = x
        n = 0
        while x1 > 0:
            n = (x1 % 10) + (n * 10)
            x1 = int(x1/10)
        return n == x
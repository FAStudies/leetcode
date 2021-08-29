class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = 1
        if x < 0:
            x = -x
            s = -1
        return x == (int(str(x)[::-1])*s)
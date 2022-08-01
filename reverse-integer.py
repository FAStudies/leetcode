class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        mult = 1
        while(x!=0):
            if x < 0:
                mult = -1
                x *= -1
            reversed = (10 * reversed) + x % 10
            x = int(x/10)
        if reversed <= -2*31 or reversed >=2**31: return 0
        return reversed * mult
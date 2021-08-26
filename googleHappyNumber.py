# https://www.youtube.com/watch?v=gW4hSbRoQoY&list=PLi9RQVmJD2fb6YDvgO2jXyIoab1FjZalf&index=2
# https://leetcode.com/problems/happy-number/submissions/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while (n != 1):
            current = n
            sum = 0
            while (current != 0):
                sum += (current % 10)*(current % 10)
                current = int(current/10)
            if sum in seen:
                return False
            seen.add(sum)
            n = sum
        return True

class Solution:
    def myAtoi(self, s: str) -> int:
        n = 0
        sgn = 1
        brk = False
        for ch in s:
            if ch == "+":
                if brk==True: break
                brk=True
                continue
            if ch == "-":
                if brk==True: break
                sgn = -1
                brk=True
                continue
            if ch == " ":
                if brk==True: break
                continue
            if ch not in ["1","2","3","4","5","6","7","8","9","0"]:
                break
            n = n*10 + int(ch)
            brk = True

        n *= sgn
        if n < -2**31:
            return -2**31
        if n > 2**31 - 1:
            return 2**31 - 1
        return n
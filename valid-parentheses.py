class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in ")}]":
                if len(stack)==0: return False
                popped = stack.pop()
                if popped=="(" and c==")":
                    continue
                if popped=="[" and c=="]":
                    continue
                if popped=="{" and c=="}":
                    continue
                else:
                    return False
            else:
                stack.append(c)
        if len(stack)!=0:
            return False
        return True
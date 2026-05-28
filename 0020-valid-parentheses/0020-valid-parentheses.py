class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        couple = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in couple:
                stack.append(c)
            elif c in couple.values():
                if not stack:
                    return False
                if c != couple[stack.pop()]:
                    return False
            else:
                return False
        return not stack
        
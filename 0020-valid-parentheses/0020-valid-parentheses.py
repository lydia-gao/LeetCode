class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        couple = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for c in s:
            if c in couple:
                stack.append(c)
            else:
                if not stack or c != couple[stack.pop()]:
                    return False

        return not stack
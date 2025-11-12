class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub = 0
        for ch in t:
            if sub == len(s):
                return True
            elif ch == s[sub]:
                sub += 1
        return sub == len(s)

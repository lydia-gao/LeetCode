class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        finding = 0
        for i in range(len(t)):
            if finding == len(s):
                return True
            if s[finding] == t[i]:
                finding += 1
        return finding == len(s)
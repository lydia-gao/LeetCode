from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = Counter(t)
        missing = len(t)

        left = 0
        res = (float("inf"), 0, 0)

        for right in range(len(s)):
            c = s[right]
            if have[c] > 0:
                missing -= 1
            have[c] -= 1

            while missing == 0:
                if right - left + 1 < res[0]:
                    res = (right - left + 1, left, right)

                lc = s[left]
                have[lc] += 1
                if have[lc] > 0:
                    missing += 1
                left += 1

        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]

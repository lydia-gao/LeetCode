from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        missing = len(t)

        left = 0
        min_len = float("inf")
        start = 0

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                left_char = s[left]
                need[left_char] += 1
                if need[left_char] > 0:
                    missing += 1
                left += 1

        return "" if min_len == float("inf") else s[start:start + min_len]

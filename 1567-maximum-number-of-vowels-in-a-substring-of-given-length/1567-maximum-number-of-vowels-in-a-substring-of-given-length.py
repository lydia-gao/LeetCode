class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vows = set('aeiuoAEIOU')
        max_vow = 0
        for i in range(k):
            if s[i] in vows:
                max_vow += 1
        window_sum = max_vow
        for i in range(1, (len(s) - k) + 1):
            if s[i - 1] in vows:
                window_sum -= 1
            if s[i + k - 1] in vows:
                window_sum += 1
            max_vow = max(max_vow, window_sum)
        return max_vow

        
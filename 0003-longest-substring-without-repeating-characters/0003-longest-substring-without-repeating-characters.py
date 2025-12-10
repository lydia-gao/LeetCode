class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        if not s:
            return 0
        left = 0
        max_count = 0
        for r in range(len(s)):
            curr = s[r]
            dic[curr] += 1
            while dic[curr] > 1:
                dic[s[left]] -= 1
                left += 1
            max_count = max(max_count, r - left + 1)
        return max_count

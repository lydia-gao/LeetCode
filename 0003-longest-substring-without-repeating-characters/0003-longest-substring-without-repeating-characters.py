class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_count = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in char_set:
                char_set.add(s[r])
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
                char_set.add(s[r])
            max_count = max(max_count, r - l + 1)

        return max_count
            
                
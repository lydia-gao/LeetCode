class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        left = 0
        delete = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                delete += 1
            while delete > 1:
                if nums[left] == 0:
                    delete -= 1
                left += 1
            window_len = i - left + 1
            if delete:
                window_len -= 1
            max_len = max(max_len, window_len)
        if delete == 0:
            max_len -= 1
        return max_len


            
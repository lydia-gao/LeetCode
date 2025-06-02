class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        left = 0
        maxl = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxl = max(maxl, i - left + 1)
        return maxl

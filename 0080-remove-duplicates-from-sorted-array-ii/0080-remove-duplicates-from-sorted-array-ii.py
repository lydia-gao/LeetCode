class Solution(object):
    def removeDuplicates(self, nums):
        pos = 2
        for curr in range(2, len(nums)):
            if nums[curr] != nums[pos - 2]:
                nums[pos] = nums[curr]
                pos += 1
        return pos

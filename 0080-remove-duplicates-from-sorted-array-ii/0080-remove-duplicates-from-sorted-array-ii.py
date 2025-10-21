class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 2
        curr = 2
        while curr < len(nums):
            if nums[curr] != nums[pos - 1] or nums[curr] != nums[pos - 2]:                
                nums[pos] = nums[curr]
                pos += 1
            curr += 1
        return pos
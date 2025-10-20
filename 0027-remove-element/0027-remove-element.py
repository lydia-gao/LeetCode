class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = len(nums) - 1
        curr = pos
        count = len(nums)
        while curr >= 0:
            if nums[curr] == val:
                count -= 1
                nums[curr] = nums[pos]
                pos -= 1
                curr -= 1
            else:
                curr -= 1
        return count

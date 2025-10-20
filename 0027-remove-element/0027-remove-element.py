class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = len(nums) - 1
        curr = 0

        while curr <= pos:
            if nums[curr] == val:
                nums[curr] = nums[pos]
                pos -= 1  # shrink valid range
            else:
                curr += 1  # move to next only if current element is kept
        return pos + 1

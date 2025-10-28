class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        longest = 0
        for i in range(0, len(nums)):
            if i > longest:
                return False
            longest = max(longest, i + nums[i])
        return True

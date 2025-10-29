class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_end = 0
        farthest = 0
        jump = 0
        for i in range(len(nums) - 1):
            curr = i + nums[i]
            farthest = max(farthest, curr)
            if curr_end >= len(nums) - 1:
                return jump
            if i == curr_end:
                curr_end = farthest
                jump += 1
                continue
            

        return jump

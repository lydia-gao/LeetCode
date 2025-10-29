class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_end = 0
        farthest = 0
        jumps = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest
                if curr_end >= len(nums) - 1:
                    return jumps

        return jumps

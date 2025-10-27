class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True

        for i in range(0, len(nums)):
            if nums[i] == 0:
                passd = False
                need = 1
                while need <= i:
                    if nums[i - need] >= need + 1:
                        passd = True
                    if i == len(nums) - 1 and nums[i - need] >= need:
                        passd = True
                    need += 1
                if not passd:
                    return False
        return True
                    

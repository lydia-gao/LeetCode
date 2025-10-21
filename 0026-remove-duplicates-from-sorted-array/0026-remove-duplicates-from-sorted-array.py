class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        curr = 1
        while curr < len(nums):
            if nums[curr] == nums[pos]:
                curr += 1
            else:
                pos += 1
                if pos != curr:
                    nums[pos] = nums[curr]
                curr += 1

        return pos + 1
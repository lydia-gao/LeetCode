class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = 0
        start = 0

        while count < n:
            curr = start
            val = nums[curr]
            while True:
                next_idx = (curr + k) % n
                val, nums[next_idx] = nums[next_idx], val
                curr = next_idx
                count += 1
                if start == curr:
                    break
            start += 1


        
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        left = 0
        res = float('inf')
        curr = 0
        for right in nums:
            curr += right
            count += 1
            if curr >= target:
                res = min(res, count)
                while curr >= target:
                    res = min(res, count)
                    count -= 1
                    curr -= nums[left]
                    left += 1

        return 0 if res == float('inf') else res
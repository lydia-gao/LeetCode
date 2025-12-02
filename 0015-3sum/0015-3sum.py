class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        if l < 3:
            return []
        res = set()
        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            curr = nums[i]
            target = - curr
            if target < curr:
                break
            left = i + 1
            right = l - 1
            while left < right:
                acc = nums[left] + nums[right]
                if acc == target:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                # skip duplicates on left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif acc < target:
                    left += 1
                else:
                    right -= 1
        return [t for t in res]


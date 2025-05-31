class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        new = sorted(nums)
        op = 0
        p1 = 0
        p2 = len(nums) - 1
        while p1 < p2:
            total = new[p1] + new[p2]
            if total == k:
                op += 1
                p1 += 1
                p2 -= 1
                continue
            else:
                if total > k:
                    p2 -= 1
                    continue
                else:
                    p1 += 1
        return op
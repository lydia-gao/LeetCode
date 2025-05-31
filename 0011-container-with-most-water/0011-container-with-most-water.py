class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        total = min(height[p1], height[p2]) * (p2 - p1)

        while p1 < p2:
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
            total = max(min(height[p1], height[p2]) * (p2 - p1), total)
        return total

        
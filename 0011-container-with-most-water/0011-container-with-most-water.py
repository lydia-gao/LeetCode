class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        best = 0
        while r > l:
            l_bar = height[l]
            r_bar = height[r]
            best = max(best, (r - l) * min(l_bar, r_bar))
            if l_bar < r_bar:
                l += 1
            else:
                r -= 1
        return best
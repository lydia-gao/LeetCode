class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        total = 0
        left = 0
        right = len(height) - 1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                if height[left] < left_max:
                    total += min(left_max, right_max) - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                if height[right] < right_max:
                    total += min(left_max, right_max) - height[right]

        return total

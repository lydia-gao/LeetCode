class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxh = 0
        curr = 0
        for num in gain:
            curr = curr + num
            maxh = max(maxh, curr)
        return maxh
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcan = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= maxcan:
                res.append(True)
            else:
                res.append(False)
        return res
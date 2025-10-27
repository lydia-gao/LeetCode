class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        small = prices[0]
        gap = 0
        for n in prices:
            if n > small:
                gap = max(n - small, gap)
            elif n < small:
                small =  n

        return gap
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        small = prices[0]
        prev = prices[0]
        profit = 0
        for n in prices:
            if n <= prev:
                if prev > small:
                    profit += prev - small
            else:
                profit += n - small
            small = n
            prev = n

        return profit
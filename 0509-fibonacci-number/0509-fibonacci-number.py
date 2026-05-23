class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        def recur(num: int) -> int:
            if num < len(dp):
                return dp[num]
            else:
                res = recur(num - 1) + recur(num - 2)
                dp.append(res)
                return res
        return recur(n)

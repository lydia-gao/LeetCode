class Solution:
    def fib(self, n: int) -> int:
        def recur(num: int) -> int:
            if num == 0:
                return 0
            elif num == 1:
                return 1
            else:
                return recur(num - 1) + recur(num - 2)
        return recur(n)   

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(curr, start, count, path):
            if curr == n and count == k:
                res.append(path[:])
                return
            if curr > n or count >= k:
                return
            for i in range(start, 10):
                if curr + i > n:
                    break
                path.append(i)
                dfs(i+curr, i + 1, count + 1, path)
                path.pop()
        dfs(0, 1, 0, [])
        return res
        
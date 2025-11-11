class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(idx):
            for j in range(n):
                if isConnected[idx][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)

        return count

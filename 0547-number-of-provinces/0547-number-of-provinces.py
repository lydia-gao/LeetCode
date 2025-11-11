class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        count = 0

        def dfs(idx):
            for j in range(len(isConnected[idx])):
                if isConnected[idx][j] == 1 and not visited[j]:
                    visited[idx] = True
                    dfs(j)

        for i in range(len(isConnected)):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)
                
        return count
        
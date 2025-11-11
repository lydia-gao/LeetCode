class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            if visited[i]:
                continue
            else:
                visited[i] = True
                count += 1
            def dfs(idx):
                visited[idx] = True
                for j in range(len(isConnected[idx])):
                    if isConnected[idx][j] == 1 and not visited[j]:
                        dfs(j)
            dfs(i)
        return count
        
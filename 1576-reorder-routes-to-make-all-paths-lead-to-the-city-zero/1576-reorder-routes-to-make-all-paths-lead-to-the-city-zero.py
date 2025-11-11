from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        # Build graph with direction flag
        for a, b in connections:
            graph[a].append((b, 1))  # edge a → b (needs reversal if used)
            graph[b].append((a, 0))  # edge b → a (already correct)
        
        visited = [False] * n

        def dfs(city):
            visited[city] = True
            changes = 0
            for nei, sign in graph[city]:
                if not visited[nei]:
                    changes += sign      # count 1 if edge is pointing away from 0
                    changes += dfs(nei)
            return changes
        
        return dfs(0)

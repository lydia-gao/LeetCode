from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        height, width = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = [[False] * width for _ in range(height)]
        visited[entrance[0]][entrance[1]] = True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y, steps = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # boundary and wall check
                if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny] and maze[nx][ny] == '.':
                    # check if it's an exit
                    if nx == 0 or ny == 0 or nx == height - 1 or ny == width - 1:
                        return steps + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))

        return -1

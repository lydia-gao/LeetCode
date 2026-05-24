class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        minute = 0
        rows = len(grid)
        cols = len(grid[0])
        # can list of list be decomposed later?
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(rows):
            for j in range(cols):
                o = grid[i][j]
                if o == 1:
                    fresh += 1
                if o == 2:
                    q.append((i, j))

        while q and fresh > 0:
            minute += 1
            level_size = len(q)
            for _ in range(level_size):
                row, col = q.popleft() 
                for dr, dc in dirs:
                    curr_r = row + dr
                    curr_c = col + dc
                    if curr_r < 0 or curr_c < 0 or curr_c >= cols or curr_r >= rows or grid[curr_r][curr_c] == 2 or grid[curr_r][curr_c] == 0:
                        continue
                    grid[curr_r][curr_c] = 2
                    q.append((curr_r, curr_c))
                    fresh -= 1

        if fresh > 0:
            return -1
        return minute



        
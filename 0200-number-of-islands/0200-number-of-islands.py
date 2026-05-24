class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]
        count = 0
        width = len(grid[0])
        height = len(grid)
        visited = [[False] * width for _ in range(height)]

        def mark(row, col):
            for i in range(0, 4):
                curr_col = col + dx[i]
                curr_row = row + dy[i]
                if (curr_col < 0 or curr_row < 0 or curr_col >= width or curr_row >= height or
                    visited[curr_row][curr_col]):
                    continue
                visited[curr_row][curr_col] = True
                if grid[curr_row][curr_col] == "1":
                    mark(curr_row, curr_col)
                    
        for row in range(height):
            for col in range(width):
                if visited[row][col] == True:
                    continue
                visited[row][col] = True
                if grid[row][col] == "1":
                    count += 1
                    mark(row, col)
        
        return count




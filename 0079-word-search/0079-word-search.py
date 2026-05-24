class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]
        width = len(board[0])
        height = len(board)
        visited = [ [False] * width for _ in range(height)]

        def dfs(curr_count: int, row: int, col: int) -> bool:
            if curr_count == len(word):
                return True
            target = word[curr_count]
            visited[row][col] = True
            for i in range(0, 4):
                curr_r = row + dr[i]
                curr_c = col + dc[i]
                if curr_c < 0 or curr_r < 0 or curr_c >= width or curr_r >= height or  visited[curr_r][curr_c]:
                    continue
                if board[curr_r][curr_c] != target:
                    continue
                if dfs(curr_count + 1, curr_r, curr_c):
                    return True
            visited[row][col] = False
            return False
    
        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    if dfs(1, i, j):
                        return True
                    
        return False


            

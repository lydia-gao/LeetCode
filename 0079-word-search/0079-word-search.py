class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row: int, col: int, index: int) -> bool:
            if (
                row < 0 or col < 0
                or row >= rows or col >= cols
                or visited[row][col]
                or board[row][col] != word[index]
            ):
                return False

            if index == len(word) - 1:
                return True

            visited[row][col] = True

            for dr, dc in dirs:
                if dfs(row + dr, col + dc, index + 1):
                    return True

            visited[row][col] = False
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
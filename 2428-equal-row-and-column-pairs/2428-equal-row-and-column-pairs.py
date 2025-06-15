import math

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = {}
        col = {}
        for li in grid:
            curr = tuple(li)
            if curr not in row:
                row[curr] = 1
            else:
                row[curr] += 1

        for i in range(len(grid)):
            li = []
            for j in range(len(grid)):
                li.append(grid[j][i])
            
            curr = tuple(li)
            if curr not in col:
                col[curr] = 1
            else:
                col[curr] += 1
        
        total = 0
        for r in row.keys():
            if r in col:
                total += row[r] * col[r]

        return total
              

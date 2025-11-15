# Last updated: 11/14/2025, 10:15:56 PM
class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        counter = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = 0

            res = (
                dfs(r+1, c),
                dfs(r-1, c),
                dfs(r, c+1),
                dfs(r, c-1)
            )
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    counter += 1
                    dfs(r,c)
        return counter
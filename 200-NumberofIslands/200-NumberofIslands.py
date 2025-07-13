# Last updated: 7/12/2025, 9:11:33 PM
class Solution(object):
    def numIslands(self, grid):
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        counter = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return
            
            grid[r][c] = '0'

            res = (
                dfs(r+1,c),
                dfs(r-1,c),
                dfs(r,c+1),
                dfs(r,c-1)
            )
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    counter += 1
        return counter
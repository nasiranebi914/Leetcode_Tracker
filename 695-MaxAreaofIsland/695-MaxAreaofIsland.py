# Last updated: 7/13/2025, 12:49:20 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.counter = 0
        max_area = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            
            grid[r][c] = 0
            self.counter += 1

            res = (
                dfs(r+1,c),
                dfs(r-1,c),
                dfs(r,c+1),
                dfs(r,c-1)
            )
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.counter = 0
                    dfs(r,c)
                    max_area = max(max_area, self.counter)
        return max_area
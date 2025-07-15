# Last updated: 7/15/2025, 4:09:27 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1,0), (-1,0), (0,-1), (0,1)]
        minute = 0

        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr,nc = dr+r, dc+c
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -= 1
            minute += 1
        
        return minute if fresh is 0 else -1
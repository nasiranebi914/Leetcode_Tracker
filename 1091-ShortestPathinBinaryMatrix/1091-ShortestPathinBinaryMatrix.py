# Last updated: 10/20/2025, 9:53:42 PM
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        queue = deque()
        visited = set([(0,0)])
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        queue.append((0,0,1))

        while queue:
            r,c,path = queue.popleft()
            if r == n-1 and c == n-1:
                return path
            for dr,dc in directions:
                nr,nc = dr+r, dc+c
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    queue.append((nr,nc,path+1))
                    visited.add((nr,nc))
        return -1
        
            



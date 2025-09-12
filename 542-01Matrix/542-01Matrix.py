# Last updated: 9/12/2025, 2:49:23 PM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        rows = len(mat)
        cols = len(mat[0])
        seen = set([])
        res = []

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c,0))
                    seen.add((r,c))
        
        directions = [(1,0), (-1,0),(0,-1), (0,1)]

        while queue:
            r,c,path = queue.popleft()
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if 0<=nr<rows and 0<=nc<cols and mat[nr][nc] != 0 and (nr,nc) not in seen:
                    mat[nr][nc] = path+1
                    seen.add((nr,nc))
                    queue.append((nr,nc,path+1))
        return mat
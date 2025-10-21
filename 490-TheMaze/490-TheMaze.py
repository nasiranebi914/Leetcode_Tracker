# Last updated: 10/21/2025, 12:37:14 PM
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = deque()
        queue.append(start)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = []
        visited.append(start)
        rows = len(maze)
        cols = len(maze[0])

        while queue:
            r,c = queue.popleft()
            if r == destination[0] and c == destination[1]:
                return True
            
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                while 0<=nr<rows and 0<=nc<cols and maze[nr][nc] == 0:
                    nr += dr
                    nc += dc
                nr -= dr
                nc -= dc
                if [nr,nc] not in visited:
                    queue.append([nr,nc])
                    visited.append([nr,nc])
        return False
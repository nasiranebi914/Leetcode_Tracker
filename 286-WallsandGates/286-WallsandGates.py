# Last updated: 7/15/2025, 2:13:12 PM
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        queue = deque()
        rows = len(rooms)
        cols = len(rooms[0])

        # Add the index of the gates to the queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        # From each gate, go 4 directions and mark INK indexes by the distance
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        while queue:
            r,c = queue.popleft()
            
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc

                if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c]+1
                    queue.append((nr,nc))

# Last updated: 7/22/2025, 8:38:59 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        # visited sets
        pacific = set()
        atlantic = set()

        # dfs function
        def dfs(r, c, visited, prevHeight):
            # Base case: out of bounds & if current height smaller than previous height
            if ((r,c) in visited or 
            r < 0 or r >= rows or c < 0 or c >= cols 
            or heights[r][c] < prevHeight):
                return
            
            visited.add((r,c))

            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        # Go inside from first and last row
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        # Go inside from first and last column
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])

        res = []
        # Add to result
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

        
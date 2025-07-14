# Last updated: 7/14/2025, 3:31:56 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        start_color = image[sr][sc]

        # If the checking node is the same and the to-be-changed color, no need to check further
        if color == start_color:
            return image

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
                return
            image[r][c] = color

            res = (
                dfs(r+1,c),
                dfs(r-1,c),
                dfs(r,c+1),
                dfs(r,c-1)
            )
        dfs(sr,sc)
        return image
            
                
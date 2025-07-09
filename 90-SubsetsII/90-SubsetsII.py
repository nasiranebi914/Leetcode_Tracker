# Last updated: 7/8/2025, 9:45:57 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def backtrack(r, c, i):
            # base case 1: i tracks how many matches we had so far
            if i == len(word):
                return True
            # base case 2: if r and c are out of bounds or invalid chars
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
            (r,c) in visited or board[r][c] != word[i]):
                return False
            # add visited r and c to visited
            visited.add((r,c))
            # explore all the directions
            res = (
                backtrack(r+1,c,i+1) or
                backtrack(r-1,c,i+1) or
                backtrack(r,c+1,i+1) or
                backtrack(r,c-1,i+1)
                )
            # undo choce
            visited.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False



# Last updated: 10/20/2025, 10:48:49 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def mark(r,c):
            if r>=rows or r<0 or c>=cols or c<0 or board[r][c]!='O':
                return
            board[r][c] = 'Z'
            res = (
                mark(r+1,c),
                mark(r-1,c),
                mark(r,c+1),
                mark(r,c-1)
            )
            return res
        # mark the borders
        for c in range(cols):
            mark(0,c)
            mark(rows-1,c)
        for r in range(rows):
            mark(r,cols-1)
            mark(r,0)
        
        # remark
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = 'X'
                if board[r][c] == 'Z':
                    board[r][c] = 'O'


        
        
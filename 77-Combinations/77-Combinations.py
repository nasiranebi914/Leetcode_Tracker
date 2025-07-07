# Last updated: 7/7/2025, 4:47:26 PM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n+1):
                # choose
                path.append(i)
                # explore
                backtrack(i+1, path)
                # undo
                path.pop()
        backtrack(1, [])
        return res
        
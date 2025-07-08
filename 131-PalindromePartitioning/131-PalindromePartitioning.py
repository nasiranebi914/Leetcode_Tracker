# Last updated: 7/8/2025, 5:44:15 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, path):
            # base case
            if start == len(s):
                res.append(path[:])
                return
            for c in range(start, len(s)):
                # choose
                sub = s[start:c+1]
                if sub == sub[::-1]:
                    path.append(sub)
                    # explore
                    backtrack(c+1, path)
                    # undo
                    path.pop()
        backtrack(0, [])
        return res
        
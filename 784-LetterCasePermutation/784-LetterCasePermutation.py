# Last updated: 7/7/2025, 3:42:57 PM
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(index, path):
            # base case
            if len(path) == len(s):
                res.append(path[:])
                return
            
            char = s[index]
            # choose, explore
            if char.isalpha():
                backtrack(index+1, path + char.upper())
                backtrack(index+1, path + char.lower())
            else:
                backtrack(index+1, path + char)
        
        backtrack(0, "")
        return res
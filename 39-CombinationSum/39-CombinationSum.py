# Last updated: 7/7/2025, 5:22:37 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, rest, path):
            # if 0, add to res
            if rest == 0:
                res.append(path[:])
                return
            # if < 0, means does not add up to target
            if rest < 0:
                return
            
            for i in range(start, len(candidates)):
                # choose
                path.append(candidates[i])
                # explore
                # i: add i instead of i+1 to be able to reuse the current number
                # rest - condidates[i]: because we want to minus the current number everytime
                backtrack(i, rest - candidates[i], path)
                # undo
                path.pop()
        
        backtrack(0,target,[])
        return res

        
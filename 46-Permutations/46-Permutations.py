# Last updated: 7/7/2025, 3:15:12 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(used, path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                # choose
                if nums[i] in used:
                    continue
                else:
                    path.append(nums[i])
                    used.append(nums[i])
                # explore
                backtrack(used, path)
                # undo
                path.pop()
                used.pop()

        backtrack([], [])
        return res

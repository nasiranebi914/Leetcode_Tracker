# Last updated: 8/19/2025, 3:38:13 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
        backtrack([])
        return res

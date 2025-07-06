# Last updated: 7/6/2025, 12:39:41 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def backtrack(start, path):
            self.res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return self.res
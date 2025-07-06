# Last updated: 7/6/2025, 3:58:50 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if (mask >> i) & 1:
                    subset.append(nums[i])
            res.append(subset)

        return res
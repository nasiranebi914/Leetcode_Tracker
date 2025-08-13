# Last updated: 8/12/2025, 8:32:50 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        money = 0
        h1 = 0
        h2 = 0

        for i in range(len(nums)):
            money = max(nums[i] + h1, h2)
            h1 = h2
            h2 = money
        return money

        
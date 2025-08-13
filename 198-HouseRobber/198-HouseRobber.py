# Last updated: 8/13/2025, 3:58:09 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        house1 = 0
        house2 = 0
        money = 0

        for i in range(len(nums)):
            money = max(nums[i] + house1, house2)
            house1 = house2
            house2 = money
        return money
        
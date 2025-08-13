# Last updated: 8/13/2025, 4:20:47 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        money1 = 0
        money2 = 0
        house1 = 0
        house2 = 0
        for i in range(len(nums)-1):
            money1 = max(nums[i] + house1, house2)
            house1 = house2
            house2 = money1
        
        house1 = 0
        house2 = 0

        for i in range(1, len(nums)):
            money2 = max(nums[i] + house1, house2)
            house1 = house2
            house2 = money2
        
        return max(money1, money2)
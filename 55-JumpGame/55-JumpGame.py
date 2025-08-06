# Last updated: 8/5/2025, 8:43:13 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return True if goal is 0 else False
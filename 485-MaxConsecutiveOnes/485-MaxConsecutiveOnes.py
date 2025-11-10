# Last updated: 11/10/2025, 5:25:07 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        left=right=0

        while left < len(nums):
            if nums[left] == 1:
                right = left+1
                while right < len(nums) and nums[right] == 1:
                    right += 1
                max_count = max(max_count, right-left)
                left = right
            else:
                left += 1
        return max_count
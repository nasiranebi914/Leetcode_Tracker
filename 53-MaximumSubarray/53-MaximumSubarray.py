# Last updated: 8/6/2025, 4:55:57 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for right in range(len(nums)):
            if current_sum < 0:
                current_sum = 0
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)
        return max_sum

        
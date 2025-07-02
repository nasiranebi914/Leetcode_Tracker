# Last updated: 7/2/2025, 2:54:47 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        max_average = float('-inf')
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            if (right - left + 1) == k:
                max_average = max(max_average, current_sum / k)
                current_sum -= nums[left]
                left += 1
        return max_average


        
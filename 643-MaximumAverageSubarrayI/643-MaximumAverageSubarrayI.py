# Last updated: 12/15/2025, 11:17:24 AM
1class Solution:
2    def findMaxAverage(self, nums: List[int], k: int) -> float:
3        left = 0
4        max_average = float('-inf')
5        current_sum = 0
6
7        for right in range(len(nums)):
8            current_sum += nums[right]
9            if (right - left + 1) == k:
10                max_average = max(max_average, current_sum / k)
11                current_sum -= nums[left]
12                left += 1
13        return max_average
14
15
16        
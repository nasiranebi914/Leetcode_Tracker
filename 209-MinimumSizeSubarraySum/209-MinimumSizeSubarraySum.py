# Last updated: 6/17/2025, 10:34:50 PM
class Solution(object):
    def minSubArrayLen(self, target, nums):
        start = end = 0
        sums = 0
        min_sum = float('inf')

        while end < len(nums):
            sums += nums[end]
            end += 1

            # shrink window while sum is valid
            while sums >= target:
                min_sum = min(min_sum, end - start)
                sums -= nums[start]
                start += 1

        return 0 if min_sum == float('inf') else min_sum



        
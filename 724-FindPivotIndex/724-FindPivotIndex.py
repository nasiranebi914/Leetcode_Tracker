# Last updated: 6/17/2025, 10:34:30 PM
class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for j,num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return j
            left_sum += num
        return -1
        
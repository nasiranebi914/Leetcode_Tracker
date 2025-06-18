# Last updated: 6/17/2025, 10:34:54 PM
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
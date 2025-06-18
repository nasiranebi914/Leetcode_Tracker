# Last updated: 6/17/2025, 10:35:09 PM
class Solution(object):
    def removeDuplicates(self, nums):
        l = r = 2
        while r < len(nums):
            if nums[r] != nums[l-2]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
        
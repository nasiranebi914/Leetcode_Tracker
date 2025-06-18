# Last updated: 6/17/2025, 10:34:55 PM
class Solution(object):
    def majorityElement(self, nums):
        counter = {}
        p = 0
        while p < len(nums):
            if nums[p] in counter:
                counter[nums[p]] += 1
            else:
                counter[nums[p]] = 1
            if counter[nums[p]] > len(nums)/2:
                return nums[p]
            p += 1
        
        
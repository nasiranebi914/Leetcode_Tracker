# Last updated: 6/17/2025, 10:35:54 PM
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i,num in enumerate(nums):
            rest = target - num
            if rest in seen:
                return [i, seen[rest]]
            seen[num] = i
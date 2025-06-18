# Last updated: 6/17/2025, 10:34:41 PM
class Solution(object):
    def findDuplicate(self, nums):
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i in seen:
            if seen[i] > 1:
                return i
            
# Last updated: 7/10/2025, 8:22:43 PM
class Solution(object):
    def findDuplicate(self, nums):
        seen = {}
        for i in nums:
            if i in seen:
                return i
            else:
                seen[i] = 1
       
            
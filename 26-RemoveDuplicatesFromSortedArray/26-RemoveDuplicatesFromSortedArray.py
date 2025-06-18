# Last updated: 6/17/2025, 10:35:15 PM
class Solution(object):
    def removeDuplicates(self, nums):
        i=j=1
        while j < len(nums):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
            j+=1
        return i

        
        
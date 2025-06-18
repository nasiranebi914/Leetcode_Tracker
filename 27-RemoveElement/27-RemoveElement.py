# Last updated: 6/17/2025, 10:35:15 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        return j
        
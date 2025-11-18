# Last updated: 11/18/2025, 2:40:38 PM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i,j = 0,len(nums)-1
        while i < j:
            mid = (i+j) // 2
            
            if nums[mid] == nums[mid+1]:
                if (j-mid)%2 == 0:
                    i = mid+1
                else:
                    j = mid-1
            elif nums[mid] == nums[mid-1]:
                if (j-mid)%2 == 0:
                    j = mid-2
                else:
                    i = mid+1
            else:
                return nums[mid]

        return nums[i]
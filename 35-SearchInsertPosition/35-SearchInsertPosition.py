# Last updated: 6/20/2025, 5:17:44 PM
class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        j = len(nums)-1

        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
            if nums[mid] > target:
                j = mid - 1
        return j+1
        
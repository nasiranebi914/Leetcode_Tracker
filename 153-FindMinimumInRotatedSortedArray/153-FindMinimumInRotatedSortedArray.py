# Last updated: 6/17/2025, 10:34:59 PM
class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if left == right:
                return nums[mid]
            if nums[mid] < nums[right]:
                right = mid # don't skip mid cause mid could also be the minimum
            if nums[mid] > nums[right]:
                left = mid+1
        
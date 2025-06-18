# Last updated: 6/17/2025, 10:34:29 PM
class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        for i in range(len(nums)):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return -1


        
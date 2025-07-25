# Last updated: 7/10/2025, 4:12:20 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums)  % 2 != 0:
            return nums[len(nums)//2]
        else:
            mid1 = nums[len(nums) // 2]
            mid2 = nums[len(nums) // 2 - 1]
            return (mid1 + mid2)/2
        return 0
        
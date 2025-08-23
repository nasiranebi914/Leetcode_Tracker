# Last updated: 8/22/2025, 9:37:27 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2 

        i = len(nums1)-1
        j = len(nums2)-1
        k = m-1
        while j >= 0:
            if k >= 0 and nums1[k] > nums2[j]:
                nums1[i] = nums1[k]
                k-= 1
            else:
                nums1[i] = nums2[j]
                j -= 1
            i -= 1

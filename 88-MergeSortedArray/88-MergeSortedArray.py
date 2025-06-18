# Last updated: 6/17/2025, 10:35:06 PM
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()
        
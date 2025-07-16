# Last updated: 7/16/2025, 2:06:25 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums1)

        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                j = stack.pop()
                if nums2[j] in nums1:
                    index = nums1.index(nums2[j])
                    ans[index] = nums2[i]
            stack.append(i)
        return ans

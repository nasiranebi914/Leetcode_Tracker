# Last updated: 6/17/2025, 10:34:33 PM
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = [-1] * (len(nums1))
        stack = []
        index = {}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if nums2[i] in nums1:
                if not stack:
                    index[nums2[i]] = -1
                else:
                    index[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        
        for i,num in enumerate(nums1):
            if num in index:
                ans[i] = index[num]
        return ans

        
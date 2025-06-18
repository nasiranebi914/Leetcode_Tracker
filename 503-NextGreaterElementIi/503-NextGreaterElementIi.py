# Last updated: 6/17/2025, 10:34:34 PM
class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        n = len(nums)
        ans = [-1] * n

        for i in range(n * 2 -1, -1, -1):
            actual_index = i % n

            while stack and stack[-1] <= nums[actual_index]:
                stack.pop()
            if not stack:
                ans[actual_index] = -1
            else:
                ans[actual_index] = stack[-1]
            stack.append(nums[actual_index])
        return ans
        
# Last updated: 9/12/2025, 12:06:02 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                h = stack.pop()
                if stack:
                    left = stack[-1]
                    water += (min(height[left], height[i]) - height[h])* (i-left-1)
            stack.append(i)
        return water

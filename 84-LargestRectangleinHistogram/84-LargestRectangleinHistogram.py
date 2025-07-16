# Last updated: 7/16/2025, 4:49:22 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index,height)
        ans = [0] * (len(heights))
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            # ones we find the a smaller height, we pop the stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index) # height is the taller one's height because we are calculating its max area before it goes away
                max_area = max(max_area, area)
                start = index
            # after popping stack, current height's index can extend all the way to the pop's index
            stack.append((start,h))
        
        # After the first round, we still have left out on the stack
        for i, h in stack:
            area = h * (len(heights)-i)
            max_area = max(max_area, area)
        return max_area
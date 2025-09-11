# Last updated: 9/10/2025, 8:37:58 PM
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        counter = 0
        for i in range(len(heights)):
            while stack and heights[i] > heights[stack[-1]]:
                j = stack.pop()
                res[j] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res
            

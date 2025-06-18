# Last updated: 6/17/2025, 10:34:30 PM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        ans = [0] * (len(temperatures))

        for i in range(len(temperatures)-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if not stack:
                ans[i] = 0
            else:
                ans[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return ans
        
# Last updated: 6/17/2025, 10:34:25 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        ans=size = 0

        for i in s:
            if i == "(":
                size+=1
                ans = max(ans, size)
            elif i == ")":
                size-=1
        return ans
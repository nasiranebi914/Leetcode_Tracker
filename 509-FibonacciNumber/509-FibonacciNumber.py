# Last updated: 8/12/2025, 3:16:40 PM
class Solution:
    cache = {0:0, 1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        for i in range(3, n+1):
            self.cache[i] = self.cache[i-1] + self.cache[i-2]
        return self.cache[n]

        
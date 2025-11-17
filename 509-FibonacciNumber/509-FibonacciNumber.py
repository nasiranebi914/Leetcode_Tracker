# Last updated: 11/17/2025, 1:43:53 PM
class Solution:
    def fib(self, n: int) -> int:
        cache = {0:0, 1:1, 2:1}
        for i in range(3,n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
        
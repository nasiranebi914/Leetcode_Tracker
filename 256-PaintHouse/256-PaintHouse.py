# Last updated: 8/13/2025, 6:13:12 PM
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        cache = [[0]*3 for _ in range(n)]
        cache[0] = costs[0][:]
        
        for i in range(1, n):
            cache[i][0] = costs[i][0] + min(cache[i-1][1], cache[i-1][2])
            cache[i][1] = costs[i][1] + min(cache[i-1][0], cache[i-1][2])
            cache[i][2] = costs[i][2] + min(cache[i-1][0], cache[i-1][1])
            cache = cache
        return min(cache[n-1])
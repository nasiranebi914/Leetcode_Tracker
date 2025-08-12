# Last updated: 8/12/2025, 4:59:29 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]

        i = cost[0]
        j = cost[1]
        
        for stair in range(2, n):
            current = cost[stair] + min(i, j)
            i, j = j, current
        return min(i, j)
        
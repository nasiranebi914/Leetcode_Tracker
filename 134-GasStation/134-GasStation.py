# Last updated: 8/7/2025, 1:47:13 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if total gas is smaller than total cost, we don't need to start
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        start = 0
        tank = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i+1
                tank = 0
        return start
                

        
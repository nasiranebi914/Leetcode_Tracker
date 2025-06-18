# Last updated: 6/17/2025, 10:34:25 PM
import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        result = float('inf')
        
        while left <= right:
            mid = (left+right)//2
            s = sum([math.ceil(float(i)/mid) for i in piles])
            if s <= h:
                result = min(result, mid)
                right = mid-1
            if s > h:
                left = mid+1
        return result
        
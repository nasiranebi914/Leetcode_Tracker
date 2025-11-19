# Last updated: 11/18/2025, 11:04:38 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # array for look up
        n = len(nums)
        lookup = [False] * (n+1)

        # mark the existing numbers
        for i in nums:
            if 0 < i <= n:
                lookup[i] = True
        
        # in the range of all the numbers from 1-n, see which one is not in lookup
        for i in range(1, n+1):
            if not lookup[i]:
                return i
        return n+1

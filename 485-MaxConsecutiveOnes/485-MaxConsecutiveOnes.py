# Last updated: 11/10/2025, 5:29:17 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        counter = 0

        for n in nums:
            if n == 1:
                counter += 1
            else:
                max_count = max(max_count, counter)
                counter = 0
        return max(max_count, counter)

# Last updated: 6/17/2025, 10:34:35 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                max_length = max(counter, max_length)
                counter = 0

        return max(max_length, counter)
        
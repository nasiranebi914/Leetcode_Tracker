# Last updated: 6/17/2025, 10:35:05 PM
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = sorted(nums)
        max_len = 1
        counter = 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                counter += 1
            elif nums[i] == nums[i + 1]:
                continue  # skip duplicate
            else:
                counter = 1  # reset

            max_len = max(max_len, counter)

        return max_len
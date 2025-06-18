# Last updated: 6/17/2025, 10:35:19 PM
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]: # avoid duplicates
                continue
            i = k+1
            j = len(nums)-1
            while i < j:
                current_sum = nums[k]+nums[i]+nums[j]
                if current_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i<j and nums[i] == nums[i-1]: # avoid duplicated i
                        i += 1
                    while i < j and nums[j] == nums[j+1]: # avoid duplicated j
                        j -= 1
                elif current_sum > 0:
                    j -= 1
                elif current_sum < 0:
                    i += 1
        return result
        
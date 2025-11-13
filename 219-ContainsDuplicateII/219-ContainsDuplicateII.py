# Last updated: 11/13/2025, 5:12:56 PM
class Solution(object):
    '''
    Problem: if nums[i] == nums[j] and distance of them <= k, return True; else False
    '''
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and i != seen[nums[i]]:
                distance = abs(i - seen[nums[i]])
                if distance <= k:
                    return True
            seen[nums[i]] = i
        return False
        
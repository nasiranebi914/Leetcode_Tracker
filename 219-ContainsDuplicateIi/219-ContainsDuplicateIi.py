# Last updated: 6/17/2025, 10:34:47 PM
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen={}
        for i, num in enumerate(nums):
            if num in seen:
                distance = i - seen[num]
                print(distance)
                if distance <= k:
                    return True
            seen[num] = i
        return False
# Last updated: 8/14/2025, 1:38:15 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = set()
        left = 0

        for right in range(len(nums)):
            if nums[right] in seen:
                return True
            seen.add(nums[right])
            if len(seen) > k:
                seen.remove(nums[left])
                left += 1
        return False
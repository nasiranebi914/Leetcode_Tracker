# Last updated: 6/17/2025, 10:34:48 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen: return True
            seen.add(i)
        return False
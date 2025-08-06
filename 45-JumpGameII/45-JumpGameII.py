# Last updated: 8/6/2025, 2:19:09 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest = 0
        current_end = 0
        steps = 0
        for i in range(len(nums)-1):
            furthest = max(furthest, nums[i] + i)
            if i == current_end:
                steps += 1
                current_end = furthest
        return steps
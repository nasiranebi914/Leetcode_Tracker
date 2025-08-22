# Last updated: 8/22/2025, 3:15:55 PM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for num in range(left, right+1):
            res += self.nums[num]
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
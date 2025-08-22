# Last updated: 8/22/2025, 3:20:09 PM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.nums)
        res = [0] * (n+1)
        for i in range(left, right+1):
            res[i+1] = res[i] + self.nums[i]
        return res[i+1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
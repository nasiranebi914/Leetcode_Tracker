# Last updated: 6/17/2025, 10:34:39 PM
class NumArray(object):

    def __init__(self, nums):
        self.prefix = self.add_to_prefix(nums)


    def add_to_prefix(self, nums):
        prefix = [0] * (len(nums) + 1)
        for i,num in enumerate(nums):
            prefix[i+1] = prefix[i] + num
        return prefix
        

    def sumRange(self, left, right):
        return self.prefix[right+1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
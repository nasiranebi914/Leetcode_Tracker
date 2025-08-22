# Last updated: 8/22/2025, 2:13:23 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        input: array of numbers in range [0,n] ; n is len(nums)
        output: only number missing from the range

        example:
        input: [1,2,3,4,5] n=5, range=[0,5]
        complete array: [0,1,2,3,4,5]
        missing number: 0
        '''
        n = len(nums)
        for i in range(0, n+1):
            if i not in nums:
                return i


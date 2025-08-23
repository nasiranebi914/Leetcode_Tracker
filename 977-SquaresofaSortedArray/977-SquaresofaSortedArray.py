# Last updated: 8/22/2025, 10:45:21 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        Questions: what is the range of numbers? any non-number elements?
        input: array sorted 
        output: new sorted array with squares of old array

        brute force:
        - for loop, calculate sqrt of each element add to res
        - sort res
        O(nlogn), O(n) n is length of array
        '''
        i = 0
        j = len(nums)-1
        res = [0] * len(nums)
        for k in range(len(nums)-1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] ** 2
                i += 1
            else:
                res[k] = nums[j] ** 2
                j -= 1
        return res
        
        
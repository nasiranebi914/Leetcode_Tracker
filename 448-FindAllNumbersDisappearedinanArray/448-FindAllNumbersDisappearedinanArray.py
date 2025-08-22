# Last updated: 8/22/2025, 2:39:07 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        questions:
        - can we have duplicates? can array be empty? can it be equal to n?
        input: 
            array nums of n integers
            >> each number is in range[1,n]
            [4,3,2,7,8,2,3,1] n=8
        output:
            array of all integers that are not in nums
        '''
        h = {}
        for i in nums:
            h[i] = 1
        res = []
        for i in range(1, len(nums)+1):
            if i not in h:
                res.append(i)
        return res
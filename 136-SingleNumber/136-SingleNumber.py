# Last updated: 8/22/2025, 3:01:38 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ''' 
        questions: range is then [1,n]? we have all duplicated except one unique?
        input:
        array, not empty, ther is only one unique element, rest are all duplicated
        need to implement in O(n), space only O(1)
        example: [3,2,1,2,4,3] > return 4
        output:
        the unique element
        '''
        # use a hashmap
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1
        for key in seen:
            if seen[key] == 1:
                return key
        
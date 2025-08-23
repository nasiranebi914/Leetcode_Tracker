# Last updated: 8/22/2025, 7:24:31 PM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        Questions: can array be empty? what if target is not there? what if there is the same char as t?
        Input: an array of chars, at least 2 chars that are different
        Output: smallest char that is lexicographically greater than target

        [c,f,d,a] target = b >> c
        '''
        for c in letters:
            if c > target:
                return c
        return letters[0]
        '''
        i = 0
        j = len(letters)-1
        while i <= j:
            mid = (i+j)//2
            if letters[mid] <= target:
                i = mid+1
            if letters[mid] > target:
                j = mid-1
        if i == len(letters):
            return letters[0]
        else:
            return letters[i]
        '''
        
            
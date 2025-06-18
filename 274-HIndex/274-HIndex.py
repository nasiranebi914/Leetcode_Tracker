# Last updated: 6/17/2025, 10:34:43 PM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i,c in enumerate(citations):
            if c < i+1:
                return i
        return len(citations)
        
        
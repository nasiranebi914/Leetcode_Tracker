# Last updated: 11/16/2025, 2:09:33 PM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])

        prevEnd = intervals[0][1]
        counter = 0

        for i in intervals[1:]:
            if i[0] >= prevEnd:
                prevEnd = i[1]
            else:
                prevEnd = min(prevEnd, i[1])
                counter += 1

        return counter

        

# Last updated: 11/16/2025, 2:10:25 PM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])

        prevEnd = intervals[0][1]
        counter = 0

        for i in intervals[1:]:
            if i[0] >= prevEnd:
                prevEnd = i[1]
            else:
                counter += 1

        return counter

        

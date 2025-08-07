# Last updated: 8/7/2025, 4:22:24 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Binasry Search to insert the newInterval
        i = 0
        j = len(intervals)-1
        while i <= j:
            mid = (i+j)//2
            if newInterval[0] < intervals[mid][0]:
                j = mid - 1
            else:
                i = mid + 1
        intervals.insert(i, newInterval)
        
        # Merge the overlapped intervals
        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged
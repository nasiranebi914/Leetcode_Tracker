# Last updated: 11/16/2025, 9:37:25 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        i = 0
        j = len(intervals)-1

        while i <= j:
            mid = (i+j)//2
            if intervals[mid][0] < newInterval[0]:
                i = mid+1
            else:
                j = mid-1
        intervals.insert(i, newInterval)

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged
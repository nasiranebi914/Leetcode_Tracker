# Last updated: 8/13/2025, 9:01:13 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda x : x[0])
        
        start = sorted([i[0] for i in intervals])
        end = sorted([j[1] for j in intervals])

        counter = 0
        res = 0
        s = 0
        e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                counter += 1
            else:
                e += 1
                counter -= 1
            res = max(res, counter)
        return res
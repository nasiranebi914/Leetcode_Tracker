# Last updated: 8/22/2025, 5:56:39 PM
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x : x[0])
        prevEnd = intervals[0][1]
        for i in intervals[1:]:
            if i[0] >= prevEnd:
                prevEnd= i[1]
            else:
                return False
        return True

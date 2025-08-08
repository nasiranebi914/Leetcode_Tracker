# Last updated: 8/8/2025, 2:47:57 PM
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x : x[0])
        prevEnd = intervals[0][1]
        for i in intervals[1:]:
            if prevEnd <= i[0]:
                prevEnd = i[1]
            else:
                return False
        return True
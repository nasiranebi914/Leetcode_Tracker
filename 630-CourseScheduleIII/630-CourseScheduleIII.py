# Last updated: 11/16/2025, 1:56:57 PM
class Solution(object):
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True
        # if there is overlapp, return False
        intervals.sort(key = lambda x:x[0])
        prevEnd = intervals[0][1]

        for i in intervals[1:]:
            if i[0] >= prevEnd:
                prevEnd = i[1]
            else:
                return False
        return True

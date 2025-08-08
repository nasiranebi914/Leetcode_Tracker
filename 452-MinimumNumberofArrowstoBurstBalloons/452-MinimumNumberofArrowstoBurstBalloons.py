# Last updated: 8/8/2025, 2:09:50 PM
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        arrow = 1
        prevEnd = points[0][1]

        for i in points[1:]:
            if prevEnd < i[0]:
                prevEnd = i[1]
                arrow += 1
            else:
                prevEnd = min(prevEnd, i[1])
        return arrow
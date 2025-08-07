# Last updated: 8/7/2025, 3:39:21 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by first index of each interval
        intervals.sort(key = lambda x : x[0])
        merged = []

        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(i[1], merged[-1][1])
        return merged
        
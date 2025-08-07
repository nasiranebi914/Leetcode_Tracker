# Last updated: 8/7/2025, 5:46:09 PM
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []

        for i in intervals:
            if i[1] < toBeRemoved[0] or i[0] > toBeRemoved[1]:
                ans.append(i)
            else:
                if i[0] < toBeRemoved[0]:
                    ans.append([i[0], toBeRemoved[0]])
                if toBeRemoved[1] < i[1]:
                    ans.append([toBeRemoved[1], i[1]])
        return ans
            
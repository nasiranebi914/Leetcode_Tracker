# Last updated: 12/3/2025, 11:17:07 AM
1class Solution:
2    def getRow(self, rowIndex: int) -> List[int]:
3        res = [[1]]
4
5        for i in range(rowIndex):
6            tmp = [0] + res[-1] + [0]
7            row = []
8            for j in range(len(res)+1):
9                row.append(tmp[j] + tmp[j+1])
10            res.append(row)
11        return res[rowIndex]
# Last updated: 12/3/2025, 11:01:29 AM
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        # start with 1
4        res = [[1]]
5
6        for i in range(numRows-1):
7            tmp = [0] + res[-1] + [0]
8            row = []
9            for j in range(len(res[-1])+1):
10                row.append(tmp[j] + tmp[j+1])
11            res.append(row)
12        return res
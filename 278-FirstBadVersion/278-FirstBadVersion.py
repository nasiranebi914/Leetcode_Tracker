# Last updated: 12/1/2025, 12:15:06 PM
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        i = 1
7        j = n
8
9        while i < j:
10            mid = (i+j)//2
11            if isBadVersion(mid):
12                j = mid
13            else:
14                i = mid+1
15        return i
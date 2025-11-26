# Last updated: 11/26/2025, 11:50:35 AM
1class Solution(object):
2    # Window Slicing problem
3    def lengthOfLongestSubstring(self, s):
4        seen = {}
5        left = 0
6        max_len = 0
7
8        for right in range(len(s)):
9            if s[right] in seen and seen[s[right]] >= left:
10                left = seen[s[right]] + 1
11            seen[s[right]] = right
12            max_len = max(max_len, right-left+1)
13        return max_len
14
15
16        
# Last updated: 11/26/2025, 11:50:57 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = {}
4        max_len = 0
5        left = 0
6
7        for right in range(len(s)):
8            if s[right] in seen and seen[s[right]] >= left:
9                left = seen[s[right]]+1
10            seen[s[right]] = right
11            max_len = max(max_len, right-left+1)
12        return max_len
13
14
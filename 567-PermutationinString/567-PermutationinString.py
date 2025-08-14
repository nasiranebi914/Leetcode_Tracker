# Last updated: 8/13/2025, 9:57:21 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = {}

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]]+1 # if duplicated, move left window to one after duplicated, to start a new window basically
            seen[s[right]] = right
            max_len = max(max_len, right-left+1)
        return max_len
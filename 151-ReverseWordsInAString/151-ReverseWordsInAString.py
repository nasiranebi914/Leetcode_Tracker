# Last updated: 6/17/2025, 10:34:59 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        return (" ".join(s))
        
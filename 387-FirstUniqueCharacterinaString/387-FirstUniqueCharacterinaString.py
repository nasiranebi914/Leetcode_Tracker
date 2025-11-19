# Last updated: 11/18/2025, 10:56:57 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        res = []
        for n,f in freq.items():
            if f == 1:
                return s.index(n)
        return -1
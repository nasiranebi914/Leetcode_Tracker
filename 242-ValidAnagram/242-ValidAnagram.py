# Last updated: 6/17/2025, 10:34:44 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _s = defaultdict(int)
        _t = defaultdict(int)

        for i in s:
            _s[i] += 1
        for j in t:
            _t[j] += 1
        return _s == _t
        
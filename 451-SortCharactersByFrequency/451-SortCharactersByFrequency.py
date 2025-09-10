# Last updated: 9/10/2025, 3:57:45 PM
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        sorted_hashmap = sorted(freq.items(), key = lambda f: f[1], reverse=True)
        res = ""
        for key,value in sorted_hashmap:
            res += "".join(key*value)
        return res
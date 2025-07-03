# Last updated: 7/2/2025, 10:59:41 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        min_window = float('inf')
        mapT = defaultdict(int)
        mapS = defaultdict(int)
        left = 0
        min_start = 0

        for i in t:
            mapT[i] += 1

        for right in range(len(s)):
            mapS[s[right]] += 1

            while all(mapS[char] >= mapT[char] for char in mapT):
                if right-left+1 < min_window:
                    min_window = right-left+1
                    min_start = left

                mapS[s[left]] -= 1
                if mapS[s[left]] == 0: 
                    del mapS[s[left]]
                left += 1

        return "" if min_window == float('inf') else s[min_start:min_start+min_window]


        
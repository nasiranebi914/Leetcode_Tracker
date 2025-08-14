# Last updated: 8/14/2025, 9:33:44 AM
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s): return 0

        left = 0
        seen = set()
        counter = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])

            if right - left + 1 >= k:
                counter += 1
                seen.remove(s[left])
                left += 1
        return counter
        
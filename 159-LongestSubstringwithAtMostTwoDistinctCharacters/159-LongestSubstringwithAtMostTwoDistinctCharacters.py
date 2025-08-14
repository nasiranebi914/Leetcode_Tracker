# Last updated: 8/13/2025, 11:02:07 PM
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = 0
        left = 0
        max_len = 0
        seen = defaultdict(int)

        for right in range(len(s)):
            seen[s[right]] += 1
            while len(seen) > 2:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
            
            
# Last updated: 7/2/2025, 9:31:04 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_window = 0
        max_freq = 0
        counter = defaultdict(int)

        for right in range(len(s)):
            counter[s[right]] += 1
            max_freq = max(max_freq, counter[s[right]])

            while (right - left + 1) - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return max_window

        
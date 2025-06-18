# Last updated: 6/17/2025, 10:34:36 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        counter = defaultdict(int)
        left=0
        window_len = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            max_freq = max(counter.values())
            current_len = right-left+1

            if current_len - max_freq > k:
                counter[s[left]] -= 1
                left += 1
            window_len = max(window_len, right-left+1)
        return window_len
        

        
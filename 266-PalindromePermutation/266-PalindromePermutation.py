# Last updated: 11/17/2025, 10:51:31 PM
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = Counter(s)
        odds = 0
        for v in freq.values():
            if v % 2 != 0:
                odds += 1
        if odds <= 1:
            return True
        else:
            return False

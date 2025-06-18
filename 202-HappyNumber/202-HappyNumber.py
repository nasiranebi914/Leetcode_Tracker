# Last updated: 6/17/2025, 10:34:52 PM
class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return True
            
        
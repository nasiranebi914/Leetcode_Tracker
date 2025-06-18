# Last updated: 6/17/2025, 10:35:06 PM
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        cleaned = list(''.join(c for c in s if c.isalnum()))
        
        i = 0
        j = len(cleaned)-1
        while i < j:
            if cleaned[i] != cleaned[j]:
                return False
            i+=1
            j-=1
        return True

        
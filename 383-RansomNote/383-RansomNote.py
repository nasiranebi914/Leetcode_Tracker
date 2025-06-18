# Last updated: 6/17/2025, 10:34:37 PM
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        a = {}
        b = {}
        for i,r in enumerate(ransomNote):
            if r in a:
                a[r] += 1
            else:
                a[r] = 1
        for j,m in enumerate(magazine):
            if m in b:
                b[m] += 1
            else:
                b[m] = 1
        
        for char in a:
            if a[char] > b.get(char, 0):
                return False
        return True

        
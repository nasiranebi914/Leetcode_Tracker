# Last updated: 6/17/2025, 10:34:35 PM
class Solution(object):
    def isSubsequence(self, s, t):
        if s == "":
            return True
        i=j=0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j+=1
            i+=1
        return j == len(s)

# Last updated: 6/17/2025, 10:34:51 PM
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_t = {}
        t_s = {}
        for i,j in zip(s,t):
            if i in s_t and s_t[i] != j or j in t_s and t_s[j] != i: return False
            s_t[i] = j
            t_s[j] = i
        return True

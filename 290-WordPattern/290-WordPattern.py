# Last updated: 6/17/2025, 10:34:40 PM
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        s_p={}
        p_s={}
        for i,j in zip(pattern,s):
            if i in s_p and s_p[i]!=j or j in p_s and p_s[j]!=i:return False
            s_p[i]=j
            p_s[j]=i
        return True

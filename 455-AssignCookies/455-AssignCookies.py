# Last updated: 11/13/2025, 11:38:15 PM
class Solution(object):
    def findContentChildren(self, g, s):
        counter = 0
        i=j=0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                counter += 1
                j += 1
                i += 1
            else:
                j += 1
        return counter

        
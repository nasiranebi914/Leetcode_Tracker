# Last updated: 6/17/2025, 10:35:11 PM
class Solution(object):
    def groupAnagrams(self, strs):
        if strs is None:
            return [[""]]
        m = {}
        for i in strs:
            j = "".join(sorted(i))
            if j not in m:
                m[j] = [i]
            else:
                m[j].append(i)
        return m.values()
        
# Last updated: 11/14/2025, 1:29:06 PM
class Solution(object):
    def partitionString(self, s):
        seen = set()
        curr = ""
        counter = 1 # at least one substring exists
        for i in s:
            if i in seen:
                counter += 1
                seen = set()
            seen.add(i)
        return counter

        
# Last updated: 6/17/2025, 10:35:12 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        counter = 0
        for i in reversed(s):
            if i != " ":
                counter += 1
            else:
                break
        return counter

        
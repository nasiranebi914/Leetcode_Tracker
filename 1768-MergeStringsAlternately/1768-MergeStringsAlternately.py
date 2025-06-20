# Last updated: 6/20/2025, 4:59:25 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        i = 0
        min_len = min(len(word1), len(word2))
        while i < min_len:
            result += word1[i]
            result += word2[i]
            i += 1
        if word1:
            result += word1[i:]
        if word2:
            result += word2[i:]
        return result        
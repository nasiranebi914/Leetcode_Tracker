# Last updated: 6/17/2025, 10:35:21 PM
class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs is None:
            return ""
        prefix = strs[0] # we say the first word is the prefix
        for i in range(1, len(strs)): # checking from index 1 word
            while strs[i].find(prefix) != 0: # if can't find prefix in the next word, will return -1
                prefix = prefix[0:len(prefix)-1] # when can't find, cut prefix by one letter
                if prefix == "":
                    return ""
        return prefix


        
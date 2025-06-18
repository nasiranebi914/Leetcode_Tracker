# Last updated: 6/17/2025, 10:35:18 PM
class Solution(object):
    def isValid(self, s):
        if s is None or len(s) % 2 != 0: return False
        stack = []

        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                left = stack.pop()
                complete = left + i
                if complete not in ["()", "{}", "[]"]:
                    return False
        return not stack
        
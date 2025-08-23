# Last updated: 8/22/2025, 11:07:04 PM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        questions: do s and t contain any non alpha chars? 
        input:
        ab#c ad#c > ac,ac > true
        ab## c#d# > '','' > true
        '''
        def build(n):
            stack = []
            for c in n:
                if c != '#':
                    stack.append(c)
                else:
                    if stack:
                        stack.pop()
            return stack
        return build(s) == build(t)

        

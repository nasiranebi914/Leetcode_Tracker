# Last updated: 8/22/2025, 10:58:32 PM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        questions: do s and t contain any non alpha chars? 
        input:
        ab#c ad#c > ac,ac > true
        ab## c#d# > '','' > true
        '''
        s1 = []
        for c in s:
            '''if c == "#" and s1:
                s1.pop()
            else:
                if c != '#':
                    s1.append(c)'''
            if c != '#':
                s1.append(c)
            else:
                if s1: 
                    s1.pop()
        s2 = []
        for c in t:
            '''if c == "#" and s2:
                s2.pop()
            else:
                if c != '#':
                    s2.append(c)'''
            if c != '#':
                s2.append(c)
            else:
                if s2:
                    s2.pop()
        return s1 == s2

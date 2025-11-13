# Last updated: 11/13/2025, 4:29:11 PM
class Solution(object):
    '''
    Problem: if s2 has a permutation of s1, return True; else False
    permutation: same lenght, different order of letters : apple = lepap
    '''
    def checkInclusion(self, s1, s2):
        counter_a = Counter(s1)
        counter_b = defaultdict(int)

        left = 0

        for right in range(len(s2)):
            counter_b[s2[right]] += 1
            if right-left+1 > len(s1):
                counter_b[s2[left]] -= 1
                if counter_b[s2[left]] == 0: del counter_b[s2[left]]
                left += 1
            if right-left+1 == len(s1):
                if counter_a == counter_b:
                    return True
        return False
        
        
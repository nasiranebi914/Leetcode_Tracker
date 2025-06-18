# Last updated: 6/17/2025, 10:34:31 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
    
        counter_a = defaultdict(int)
        counter_b = defaultdict(int)
        left = 0

        for i in s1:
            counter_a[i] += 1
        
        for right in range(len(s2)):
            counter_b[s2[right]] += 1

            if right - left + 1 > len(s1):
                counter_b[s2[left]] -= 1
                if counter_b[s2[left]] == 0: del counter_b[s2[left]]
                left += 1
            
            if right - left + 1 == len(s1):
                if counter_a == counter_b:
                    return True
            
        return False




        
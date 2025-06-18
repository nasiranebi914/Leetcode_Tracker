# Last updated: 6/17/2025, 10:34:27 PM
class Solution(object):

    def ifSymmetric(self, num):
        num_str = str(num)
        left = 0
        right = len(num_str)-1
        if len(str(num)) % 2 == 0:
            left_part = 0
            right_part = 0
            while left < right:
                left_part += int(num_str[left])
                right_part += int(num_str[right])
                left += 1
                right -= 1
            if left_part == right_part:
                print(left_part, right_part)
                return True
        return False

                
    def countSymmetricIntegers(self, low, high):
        counter = 0
        for i in range(low, high+1):
            if self.ifSymmetric(i):
                counter += 1
        return counter
        
        
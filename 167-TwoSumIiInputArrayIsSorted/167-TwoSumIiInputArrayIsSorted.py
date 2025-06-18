# Last updated: 6/17/2025, 10:34:56 PM
class Solution(object):
    def twoSum(self, numbers, target):
        j = len(numbers)-1
        i = 0

        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum == target:
                return [i+1, j+1]
            elif current_sum < target:
                i += 1
            elif current_sum > target:
                j -= 1

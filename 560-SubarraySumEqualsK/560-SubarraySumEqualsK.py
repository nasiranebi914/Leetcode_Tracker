# Last updated: 6/17/2025, 10:34:32 PM
class Solution(object):
    def subarraySum(self, nums, k):
        prefix = {0:1}
        counter = 0
        current_sum = 0

        for num in nums:
            current_sum += num # sums until num
            rest = current_sum - k 
            # rest is the sum of a compliment subarray. If there is a compliment subarray, meaning there is a subarray of sum k
            if rest in prefix:
                counter += prefix[rest] 
                # so we add the frequency to the counter. If there are 2 complimented subarray, there are 2 subarray of sum k as well
            prefix[current_sum] = prefix.get(current_sum, 0) + 1 # add the frequency of current sum

        return counter


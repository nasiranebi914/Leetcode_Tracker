# Last updated: 10/13/2025, 12:00:03 PM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_sum = -1
        max_digit = defaultdict(list)

        for num in nums:
            digit = max(str(num))
            max_digit[digit].append(num)
        print(max_digit)
        
        for group in max_digit.values():
            if len(group) >= 2:
                a, b = heapq.nlargest(2, group)
                total = a+b
                max_sum = max(total, max_sum)
        return max_sum

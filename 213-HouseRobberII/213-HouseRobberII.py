# Last updated: 8/13/2025, 4:40:27 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        dp[len(nums)-2] = max(nums[n-1],nums[n-2])

        for i in range(n-3,-1,-1):
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])

        ans = dp[1]


        dp = [0] * len(nums)
        #dp[-1] = nums[-1]
        dp[len(nums)-2] = nums[n-2]

        for i in range(n-3,-1,-1):
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])

        ans = max(ans, dp[0])
        return ans
        
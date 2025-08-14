# Last updated: 8/14/2025, 9:18:11 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for price in prices:
            if price < buy:
                buy = price
            max_profit = max(max_profit, price - buy)
        return max_profit

        
# Last updated: 6/17/2025, 10:35:07 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = float('inf')

        for price in prices:
            if price < min_buy:
                min_buy = price
            else:
                max_profit = max(max_profit, price - min_buy)
        return max_profit
                
        
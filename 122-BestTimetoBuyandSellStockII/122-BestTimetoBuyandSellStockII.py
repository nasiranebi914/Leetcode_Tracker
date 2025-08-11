# Last updated: 8/11/2025, 4:30:35 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        buy = float('inf')
        total = 0
        
        for price in prices:
            if price < buy:
                buy = price
            current_profit = price - buy
            print(current_profit)
            total += current_profit
            buy = price
        return total
        


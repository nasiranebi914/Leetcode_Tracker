# Last updated: 11/14/2025, 8:40:58 PM
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_buy = float('inf')

        for price in prices:
            if price < min_buy:
                min_buy = price
            max_profit = max(max_profit, price-min_buy)
        return max_profit

        




  
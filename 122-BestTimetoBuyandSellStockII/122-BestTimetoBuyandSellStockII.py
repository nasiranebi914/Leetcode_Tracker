# Last updated: 11/14/2025, 9:09:35 PM
class Solution(object):
    def maxProfit(self, prices):
        min_buy = float('inf')
        total = 0
        for price in prices:
            if price < min_buy:
                min_buy = price
            total += price-min_buy
            min_buy = price
        return total
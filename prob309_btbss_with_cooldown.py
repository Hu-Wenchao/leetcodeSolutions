"""
Say you have an array for which the ith element is the 
price of a given stock on day i.

Design an algorithm to find the maximum profit. You may 
complete as many transactions as you like (ie, buy one 
and sell one share of the stock multiple times) with the 
following restrictions:

You may not engage in multiple transactions at the same 
time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next 
day. (ie, cooldown 1 day)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell

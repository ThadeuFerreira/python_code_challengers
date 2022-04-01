# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_possible_profit_array = [0]*len(prices)
        #go backwards through the array and add the max profit possible for each day
        for i in reversed(range(len(prices)-1)):
            max_possible_profit_array[i] = max(0, prices[i+1] - prices[i] + max_possible_profit_array[i+1])
        return max(max_possible_profit_array)

    def maxProfit2(self, prices: List[int]) -> int:
        current_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - current_min)
            current_min = min(current_min, prices[i])
        return max_profit
s = Solution()
prices = [7,2,4,1]
print(s.maxProfit(prices))
print(s.maxProfit2(prices))
prices = [2,1,4,1]
print(s.maxProfit(prices))
print(s.maxProfit2(prices))
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))
print(s.maxProfit2(prices))
prices = [7,6,5,4,3,2,1,100]
print(s.maxProfit(prices))
print(s.maxProfit2(prices))
prices = [7,6,0,4,3,2,1,100,0,200]
print(s.maxProfit(prices))
print(s.maxProfit2(prices))
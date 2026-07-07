class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        max_profit = 0
        while sell < len(prices):
            profit = prices[sell]-prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(profit,max_profit)
                sell+=1
            else:
                buy = sell
                sell+=1
        return max_profit
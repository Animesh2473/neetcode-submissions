class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            minimum = prices[i]
            for j in range(i+1,len(prices)):
                profit = prices[j]-minimum
                maximum = max(maximum,profit)
        return maximum
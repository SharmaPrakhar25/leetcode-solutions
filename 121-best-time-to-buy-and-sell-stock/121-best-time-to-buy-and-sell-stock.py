class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx] <= buyPrice:
                buyPrice = prices[idx]
            else:
                profit = max(profit, prices[idx]-buyPrice)
            
        return profit
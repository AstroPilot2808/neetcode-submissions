class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bestProfit = 0

        buy, sell = 0, 1

        while buy < len(prices) and sell < len(prices):
            bestProfit = max(prices[sell] - prices[buy], bestProfit)
            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy + 1
            else:
                sell += 1
            
        return bestProfit
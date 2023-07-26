class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        buy = -prices[0] - fee
        sell = 0
        for i in range(1, len(prices)):
            price = prices[i]
            newBuy = max(buy, sell - price - fee)
            newSell = max(sell, price + buy)
            buy, sell = newBuy, newSell
        return sell
        
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        n = len(prices)
        prices.append(float("-inf"))
        
        for i in range(n):
            p1 = prices[i]
            p2 = prices[i+1]
            if p2 > p1:
                ans += (p2 - p1)
        return ans
            
        
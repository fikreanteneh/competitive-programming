class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        n = len(prices)
        
        for i in range(n-1):
            p1 = prices[i]
            p2 = prices[i+1]
            if p2 > p1:
                ans += (p2 - p1)
        return ans
            
        
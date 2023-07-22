class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last = [0, -prices[0], 0]
        for i in range(1, len(prices)):
            price = prices[i]
            new = []
            new.append(max(last[2], last[0]))
            new.append(max(last[1], last[0] - price))
            new.append(last[1] + price)
            last = new
        
        return max(last)
            
        
#    -1 buy   1 sell  1 cool   1 buy   2 cell
#     0 cool -1 buy   2 sell   1 cool
#             0 cool -1 buy   -1 sell
                  
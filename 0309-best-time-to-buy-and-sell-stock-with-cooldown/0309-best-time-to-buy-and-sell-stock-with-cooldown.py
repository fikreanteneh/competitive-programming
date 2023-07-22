class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last = {"cool": 0, "buy": -prices[0], "sell": 0}
        for i in range(1, len(prices)):
            price = prices[i]
            new = {}
            for prev, state in last.items():
                if prev == "buy":
                    new["sell"] = state + price
                elif prev == "sell" :
                    new["cool"] = max(state, last["cool"])
                elif prev == "cool":
                    new["buy"] = max(last["buy"], state - price)
            last = new
        
        return max(last.values())
            
        
#    -1 buy   1 sell  1 cool   1 buy   2 cell
#     0 cool -1 buy   2 sell   1 cool
#             0 cool -1 buy   -1 sell
                  
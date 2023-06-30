class Solution:
    def coinChange(self, coins: List[int], amount: int ) -> int:
        memo, step = {}, 1
        x = self.calculate(coins, amount, step, memo)
        return -1 if x == float("inf") else x - 1
    def calculate(self, coins, amount, step, memo):
        if amount in memo:
            return memo[amount] + step
        elif amount == 0: 
            return step
        elif amount < 0:
            return float("inf")
        steps = float("inf") 
        for i in coins:
            x = self.calculate(coins, amount - i, step + 1, memo)
            steps = min(steps, x)
        ans = steps    
        memo[amount] = min(ans -step, memo.get(amount, float("inf")))
        return ans


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        cost.append(0)
        
        def calc(stair):
            if stair < 2:
                return cost[stair]
            
            if stair not in memo:
                x = calc(stair - 1)
                y = calc(stair - 2)
                memo[stair] = min(x + cost[stair], y + cost[stair])
            
            return memo[stair]
        
        return calc(n)
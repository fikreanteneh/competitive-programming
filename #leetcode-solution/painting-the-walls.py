class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        
        @cache
        def dp(index, remaining):
            if remaining <= 0:
                return 0
            if index >= n:
                return float("inf")
            paint = cost[index] + dp(index + 1, remaining - 1 - time[index])
            nopaint = dp(index + 1, remaining)
            return min(paint, nopaint)
        return dp(0, n)
                
                
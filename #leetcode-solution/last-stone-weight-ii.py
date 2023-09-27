class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        @cache
        def dp(index, sums):
            if index >= n:
                if sums < 0:
                    return float("inf")
                return sums
            choice1 = dp(index + 1, sums + stones[index])
            choice2 = dp(index + 1, sums - stones[index])
            return min(choice1, choice2)
        
        return dp(0, 0)
            
        
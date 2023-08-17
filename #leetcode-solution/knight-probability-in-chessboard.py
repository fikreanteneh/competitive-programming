class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [ (2, 1), (2, -1),  (-2 , 1), (-2 , -1), (1, 2), (-1, 2), (1, -2), (-1, -2) ]
        
        @cache
        def dp( r , c , curr):
            
            if not (0 <= r < n and 0 <= c < n):
                return 0
            
            if curr == k:
                return 1
            
            ans = 0 
            for x, y in directions:
                ans += dp(r + x, c + y , curr + 1)
            
            return ans
        
        return dp(row, column, 0) / (8 ** k)
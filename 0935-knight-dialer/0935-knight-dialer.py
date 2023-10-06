class Solution:
    def knightDialer(self, n: int) -> int:
        
        dest = [[4, 6], [6,8], [7, 9], [4, 8], [3,9,0], [], [1,7,0], [2,6], [1,3],[4, 2]]
        
        @cache
        def dp(index, n):
            if n <= 1:
                return 1
            possible = dest[index]
            ans = 0
            for poss in possible:
                ans += dp(poss, n - 1)
            return ans
        answer = 0
        for index in range(10):
            answer += dp(index, n)
        
        return answer % (10**9 + 7)
            
            
                
            
        
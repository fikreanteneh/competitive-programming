class Solution:
    def tribonacci(self, n: int) -> int:
        
        mapp = [0,1,1]
        memo = {}
        def calc(n):
            if n <= 2:
                return mapp[n]
            if n not in memo:
                memo[n] = calc(n-1) + calc(n-2) + calc(n-3)
            return memo[n]
        
        return calc(n)
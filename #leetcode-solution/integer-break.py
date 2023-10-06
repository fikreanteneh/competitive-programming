class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1, 1, 2, 4, 6, 9, 12]
        for i in range(8, n+1):
            dp.append( 3*dp[i - 3])
        return dp[n]
        
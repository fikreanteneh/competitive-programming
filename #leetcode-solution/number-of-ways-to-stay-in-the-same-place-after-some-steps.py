class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        arrLen = min(arrLen - 1, 500 - 1)
        @cache
        def dp(index, steps):
            if index == 0 and steps == 0:
                return 1
            if index < 0 or index > arrLen or steps == 0:
                return 0
            ans = 0
            ans += dp(index + 1, steps - 1)%MOD
            ans += dp(index - 1, steps - 1)%MOD
            ans += dp(index, steps -1)%MOD
            return ans%MOD
        return dp(0, steps)
            
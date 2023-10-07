class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0 or m < k:
            return 0
        
        # @cache
        # def dp(index, curr, needed, total):
        #     print(index, curr, "----")
        #     if curr == needed + 1:
        #         return 1
        #     ans = 0
        #     for i in range(index + 1,  total - needed + curr + 1):
        #         ans += dp(i, curr + 1, needed, total)
        #     return ans
        
        @cache
        def dp(index, increasing, largest):
            if index == n:
                if increasing == k:
                    return 1
                return 0
            
            ans = 0
            for mx in range(1, m+1):
                if mx > largest:
                    ans += dp(index + 1, increasing + 1, mx)
                else:
                    ans += dp(index + 1, increasing, largest)
            return ans
        return dp(0,0,0) % (10**9 + 7)
                
                
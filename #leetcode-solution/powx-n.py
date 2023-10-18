class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def mypow(x, n):
            if n == 1:
                return x
            if n%2:
                return mypow(x, n//2)*mypow(x, n//2)*x
            else:
                return mypow(x, n//2)*mypow(x, n//2)
        if n == 0:
            return 1
        ans = mypow(x, abs(n))
        if n < 0:
            return 1/ans
        return ans
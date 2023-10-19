class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even, odd = (n//2) + (n%2) , n//2
        @cache
        def calc(n, val):
            if n == 1:
                return val
            if n == 0:
                return 1
            return ( calc(n//2, val) * calc( (n//2) + (n%2) , val)  )%MOD
        return (calc(even, 5) * calc(odd, 4) )% MOD
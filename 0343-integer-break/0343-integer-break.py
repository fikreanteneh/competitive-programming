class Solution:
    def integerBreak(self, n: int) -> int:
        maxi = 1
        if n == 2: return 1
        if n == 3: return 2
        for i in range(1, n//2 + 1):
            y = n % i
            x = n//i
            product2 = (i**x) * y
            x = x - y
            product1 = (i**x) * ((i + 1)**y)
            maxi = max(maxi, product1, product2)
        return maxi

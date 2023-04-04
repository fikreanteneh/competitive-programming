class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        num = [True] * n
        num[0], num[1] = False, False
        r = int(sqrt(n)) + 1
        for i in range(2, r):
            if num[i]:
                for j in range(i, n//i + 1):
                    x = i * j
                    if x  < n:
                        num[x] = False
        return Counter(num)[True]
            
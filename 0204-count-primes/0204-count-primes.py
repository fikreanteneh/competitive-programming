class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        num = [i for i in range(n)]
        r = int(sqrt(n)) + 1
        for i in range(2, r):
            if num[i]:
                for j in range(i, n//i + 1):
                    x = i * j
                    if x  < n:
                        num[x] = 0
        num = set(num)
        num.discard(0)
        num.discard(1)
        return len(num)
            
class Solution: 
    def fib(self, n: int, cache = {}) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        if n in cache: return cache[n]
        cache[n] =  self.fib(n-1, cache) + self.fib(n-2, cache)
        return cache[n]

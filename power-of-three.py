class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        x = n % 3
        if x != 0 or n == 0: return False
        n //= 3
        return self.isPowerOfThree(n)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        x = n % 4
        if x != 0 or n == 0: return False
        n //= 4
        return self.isPowerOfFour(n)

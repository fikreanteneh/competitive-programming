class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        curr = 1 if n%2 == 0 else 0
        while n > 0:
            x = n & 1
            if x == curr:
                return False
            n >>= 1            
            curr = 1 - curr
        
        return True
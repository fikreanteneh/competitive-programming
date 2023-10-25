class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        for n in range(n - 1, 0, -1):
            indexes = 1 << n
            if k <= (indexes >> 1):
                continue
            k -= (indexes >>  1)
            curr = 1 - curr
        return curr
            
            
        
            
class Solution:
    def minSteps(self, n: int) -> int:
        
        
        # Math Solution
        operation = 0
        while n > 1:
            copiedFrom = n // 2
            while n % copiedFrom:
                copiedFrom -= 1
            operation += 1 # for copying
            operation +=  (n//copiedFrom - 1) # for pasting
            n = copiedFrom # next goal is reching this value
        return operation
class Solution:
    def minSteps(self, n: int) -> int:
        operation = 0
        while n > 1:
            copiedFrom = n // 2
            while n % copiedFrom:
                copiedFrom -= 1
            operation += (n // copiedFrom)
            n = copiedFrom
        return operation
class Solution:
    def minSteps(self, n: int) -> int:
        operation = 0
        while n > 1:
            i = 2
            while n % i != 0:
                i += 1
            operation += i
            n //= i
        return operation
        
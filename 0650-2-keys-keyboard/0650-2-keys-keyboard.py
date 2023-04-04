class Solution:
    def minSteps(self, n: int) -> int:
        operation = 0
        while n > 1:
            i = n// 2
            while n % i != 0:
                i -= 1
            operation += (n//i)
            n = i
        return operation
        
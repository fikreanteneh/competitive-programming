class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum = 0
        n = str(n)
        sign = 1
        for i in (n):
            sum += (sign * int(i))
            sign *= -1
        return sum
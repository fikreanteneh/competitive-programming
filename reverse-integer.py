class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: i = -1
        else: i = 1
        sum, x = 0, abs(x)
        while x > 0:
            sum = sum * 10
            sum += (x % 10)
            x //=10
        if i == -1: sum*=(-1)
        if -2**31 <= sum <= 2**31 - 1: return sum
        return 0

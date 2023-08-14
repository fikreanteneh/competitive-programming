# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int, m = 1) -> int:
        num = (n + m)//2
        g = guess(num)
        if g == 0:
            return num
        elif g == -1:
            return self.guessNumber(num - 1, m)
        else:
            return self.guessNumber(n, num + 1)
            
            
        
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))
        while i <= j:
            sums = i ** 2 + j ** 2
            if sums == c:
                return True
            elif sums > c:
                j -= 1
            else:
                i += 1
        return False
    """
    0  1  2  3 4 5
    0  0  0
    25 16 
    
    """
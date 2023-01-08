class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0
        while n > 0:
            n = n // 5
            answer += (n)
        return answer
        """
        3 2 1
        5 4 3 2 1
        7 6 5 4 3 2 1
        15 13 14 12 11 10 9 8 7 6 5 4 3 2 1
        """
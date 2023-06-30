class Solution:
    def findComplement(self, num: int) -> int:
        x = int(math.log(num, 2)) + 1
        check = (2 ** x) - 1
        return num ^ check

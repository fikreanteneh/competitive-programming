class Solution:
    def reverseBits(self, n: int) -> int:
        # n = bin(n)
        arr = []
        for i in range(32):
            if (n & (1 << i)):
                arr.append("1")
            else:
                arr.append("0")
        return int("".join(arr), 2)
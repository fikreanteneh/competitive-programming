class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            cur = 0
            checker = 1
            while checker <= i:
                if (i & checker):
                    cur += 1
                checker <<= 1
            ans.append(cur)
        return ans

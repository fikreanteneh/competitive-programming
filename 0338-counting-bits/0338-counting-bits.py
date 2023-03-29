class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            temp = i
            cur = 0
            checker = 1
            while temp:
                cur += (temp & 1)
                temp >>= 1
            ans.append(cur)
        return ans

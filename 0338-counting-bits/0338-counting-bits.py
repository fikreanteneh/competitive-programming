class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        store = {}
        for i in range(n + 1):
            temp = i
            cur = 0
            checker = 1
            while temp:
                if temp in store:
                    cur += store[temp]
                    break
                cur += (temp & 1)
                temp >>= 1
            store[i] = cur
            ans.append(cur)
        return ans

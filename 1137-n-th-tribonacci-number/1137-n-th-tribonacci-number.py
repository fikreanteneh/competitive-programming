class Solution:
    def tribonacci(self, n: int) -> int:
        
        mapp = [0,1,1]
        memo = {}
        if n <= 2:
            return mapp[n]
        for i in range(3, n + 1):
            mapp.append(mapp[i - 1] + mapp[i - 2] + mapp[i - 3])
        return mapp[n]
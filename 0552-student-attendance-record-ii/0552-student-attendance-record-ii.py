class Solution:
    def checkRecord(self, n: int) -> int:
        store = [  [[0,0,0] for _ in range(2)] for _ in range(n + 1) ]
        # the nth array has an array of [x, y, z], [x, y , z]
        # the first holds if there is no absent if there is a bsent
        # x is when the previos is not late
        # y is when the previos is exactly one late
        # z is when the previos 2 is late late
        store[1][0][0] = 1
        store[1][1][0] = 1
        store[1][0][1] = 1
        # print(store[1])
        MOD = 10**9 + 7
        
        for i in range(2, n+1):
            store[i][0][0] = (store[i - 1][0][0] + store[i - 1][0][1] + store[i - 1][0][2]) % MOD
            store[i][0][1] = store[i - 1][0][0] % MOD
            store[i][0][2] = store[i - 1][0][1] % MOD
            
            store[i][1][0] = (store[i - 1][0][0] + store[i - 1][0][1] + store[i - 1][0][2] + store[i - 1][1][0] + store[i - 1][1][1] + store[i - 1][1][2]) % MOD
            store[i][1][1] = store[i - 1][1][0] % MOD
            store[i][1][2] = store[i - 1][1][1] % MOD
            # print(store[i])
            
        return (sum(store[-1][0]) + sum(store[-1][1])) % MOD
            
            
        """
        [1,1,0], [1,0,0]
        [2,]
        """
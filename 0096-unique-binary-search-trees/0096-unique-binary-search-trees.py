class Solution:
    def numTrees(self, n: int) -> int:
        
        store = [1,1,2]
        for i in range(3, n+1):
            num = 0
            for j in range(i):
                num += (store[j] * store[i - j - 1])
            store.append(num)
        return store[n]
                
            
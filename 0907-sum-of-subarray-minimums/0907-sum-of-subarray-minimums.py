class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        prevM = [i for i in range(1, len(arr) + 1)]
        nextM = [i for i in range(len(arr), 0, -1)]
        n = len(arr) - 1
        stackN = []
        stackP = []
        
        for i, num in enumerate(arr):
            
            while stackN and stackN[-1][0] > num:
                val = stackN.pop()
                nextM[val[1]] = i - val[1]
            stackN.append((num,i))
            
            while stackP and stackP[-1][0] >= arr[n-i]:
                val = stackP.pop()
                prevM[val[1]] = val[1] - (n-i)
            stackP.append((arr[n-i],n-i))
        
        print(nextM)
        print(prevM)
        
        ans = 0
        for i in range(n + 1):
            ans += (arr[i] * prevM[i] * nextM[i])
        mod = 1000000007
        return ans % mod
                
                
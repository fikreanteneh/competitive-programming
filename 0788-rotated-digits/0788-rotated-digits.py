class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            flag = 0
            
            for j in str(i):
                if j in "2569":
                    flag = 1
                elif j in "347":
                    flag = 0
                    break
                # if i == 23: print(i,flag, j)
            ans += flag
        return ans
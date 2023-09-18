class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        self.n = len(num)
        
        
        def sol(index, prev1, prev2):
            if index == self.n:
                return True
            sums = int(prev1) + int(prev2)
            for i in range(index + 1, self.n + 1):
                if len(num[index:i]) > 1 and  num[index] == "0":
                    continue
                if int(num[index:i]) == sums and sol(i, prev2, num[index:i]):
                    return True
                    
        
        
        for i in range(1, self.n  - 1):
            for j in range(i + 1, self.n):
                if (len(num[i:j]) > 1 and  num[i] == "0") or (len(num[0:i]) > 1 and  num[0] == "0"):
                    continue
                if sol(j, num[0:i], num[i:j]):
                    return True
        
        return False
class Solution:
    def countOrders(self, n: int) -> int:
        
        answer = 1
        MOD = (10**9 + 7 )
        for i in range(1, n + 1):
            prevPickDeliver = ((i - 1) << 1) + 1
            order = (prevPickDeliver *(1 + prevPickDeliver)) >> 1 
            answer *= order
            answer %= MOD
        
        return answer
        
        
                     
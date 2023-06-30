class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        answer = 0
        
        num = [numOnes, numZeros, numNegOnes]
        val = [1, 0, -1]
        
        for j, i in enumerate(num):
            if k <= 0:
                break
            x = k if i >= k else i
            answer += (x * val[j])
            k -= x
        
        return answer
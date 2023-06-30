class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        answer = ""
        nums = [i for i in range(1, n+1)]
        k -= 1
        while nums and k >= 0:
            possible = factorial(n - 1)
            index = ceil(k // possible)
            answer = answer + str(nums.pop(index))
            n -= 1
            k -= ( (k // possible) * possible)
        
        
        return answer
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = self.solution( n)
        return str(ans[k-1])
        
        
    def solution(self,n):
        if n == 1:
            return [0]
        prev = self.solution(n - 1)
        answer = prev.copy()
        answer.append(1)
        self.reverse(prev)
        answer.extend(prev)
        return answer
        
    def reverse(self, arr):
        self.invert(arr)
        arr.reverse()
               
    def invert(self, arr):
        for i, val in enumerate(arr):
            arr[i] = 1 - val

        
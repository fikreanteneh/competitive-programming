class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
#         result= self.solution(x, abs(n))
#         return result if n > -1 else 1/result
        
#     def solution(self,x, y):
#         if y == 0:
#             return 1
#         return x * self.myPow(x, y-1)
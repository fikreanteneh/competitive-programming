class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        self.leftD = {0:0, 1:1}
        self.rightD = {0:1, 1:0}
        
        def solution(mid, right, current):
            if mid == 0 or right == 1:
                return current
            
            leftD, rightD = mid - 1, right - mid
            x = right // 2
            if leftD > rightD:
                return solution(mid - x, x, self.rightD[current])
            else:
                return solution(mid, x, self.leftD[current])
            
            
        return solution(k, 2 ** (n - 1), 0)
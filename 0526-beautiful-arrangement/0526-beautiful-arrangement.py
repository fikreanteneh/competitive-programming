class Solution:
    def countArrangement(self, n: int) -> int:
        self.beautiful = 0
        self.cur = 0
        check = (2**(n)) - 1
        
        def solution(index):
            if self.cur == check:
                self.beautiful += 1
                return
            
            for i in range(n):
                if self.cur & ( 1 << i) == 0 and (index % (i + 1) == 0 or (i + 1) % index == 0) :
                    self.cur |= (1 << i)
                    solution(index + 1)
                    self.cur ^= (1 << i)         
        
        solution(1)
        return self.beautiful
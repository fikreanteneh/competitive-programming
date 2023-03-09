class Solution:
    def splitString(self, s: str) -> bool:
        s = list(s)
        n = len(s) 
        if n == 1:
            return False
        flag = False
        
        def solution(index, upper, prev):
            # print(prev, upper, prev - upper, index, n)
            if prev - upper != 1:
                return False
            if index == n:
                return True
            for i in range(1, n - index + 1):
                temp = solution(index + i , int( "".join(s [ index:index + i])), upper)
                
                if temp:
                    return temp
            return False
            
                
            
        
        for i in range(1,n):
            # print(int("".join(s[:i])))
            flag = solution(i, int("".join(s[:i])), int("".join(s[:i])) + 1 ) or flag
            if flag:
                break
                    
        return flag
        
        
        
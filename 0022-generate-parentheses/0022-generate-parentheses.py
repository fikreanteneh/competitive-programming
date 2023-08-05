class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []
        def sol(opened, closed, curr):
            if opened == closed == 0:
                answer.append(curr)
                return
            if opened:
                sol(opened - 1, closed, curr + "(")
            if closed > opened:
                sol(opened, closed - 1, curr + ")")    
        sol(n, n, "")       
        return answer

                        
                            
                
            
        
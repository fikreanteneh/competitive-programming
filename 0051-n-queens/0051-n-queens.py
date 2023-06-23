class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        prev = []
        answer = []
        def solv(level):
            if level == n:
                organize()
            
            for i in range(0, n):
                if check(level, i):
                    prev.append(i)
                    solv(level + 1)
                    prev.pop()
                    
        def check(row, col):
            for rowO, colO in enumerate(prev):
                if abs(row - rowO) == abs(col - colO) or colO == col or rowO == row:
                    return False
            return True
        
        def organize():
            ans = []
            for pos in prev:
                row = ["."] * n
                row[pos] = "Q"
                x = "".join(row)
                ans.append(x)
            answer.append(ans)
            
        
        solv(0)
        
        return answer
            
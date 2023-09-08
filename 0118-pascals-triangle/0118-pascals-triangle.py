class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        rows = [[1]]
        
        for i in range(2,numRows+ 1):     
            upperRow = rows[-1]
            answer = [0] * ( i )
            answer[0], answer[-1] = 1, 1
            for j in range(1, i-1):
                answer[j] += (upperRow[j-1] + upperRow[j])
            rows.append(answer)
        
        return rows
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        upperRow = self.getRow(rowIndex - 1)
        
        answer = [0] * (rowIndex + 1)
        answer[0], answer[-1] = 1, 1
        
        for i in range(1, rowIndex):
            answer[i] += (upperRow[i-1] + upperRow[i])
        
        return answer
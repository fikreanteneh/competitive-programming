class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, columns = len(matrix), len(matrix[0])
        self.matrix = [[0]*(columns+1) for i in range(rows+1)]
        for i in range(rows):
            sum = 0
            for j in range(columns):
                sum += matrix[i][j]
                self.matrix[i+1][j+1] = sum + self.matrix[i][j + 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        aboveRegion = self.matrix[row1][col2+1]
        leftRegion = self.matrix[row2 +1 ][col1] 
        redundant = self.matrix[row1][col1]
        lowerRight = self.matrix[row2+1][col2+1]
        return lowerRight + redundant - leftRegion - aboveRegion
                
            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

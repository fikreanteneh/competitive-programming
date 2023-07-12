class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        self.answer = 0
        
        def calculate(row, col):
            height = 1
            width = matrix[row][col]
            
            while row >= 0 and matrix[row][col]:
                # print(row, col, matrix)
                width = min(width, matrix[row][col])
                self.answer = max(self.answer, height * width)
                height += 1
                row -= 1
                
                
        for row in range(rows):
            runSum = 0
            for col in range(cols):
                matrix[row][col] = int(matrix[row][col])
                if matrix[row][col] == 0:
                    runSum = 0
                    continue
                runSum += matrix[row][col]
                matrix[row][col] = runSum
                calculate(row, col)
                
        return self.answer
                
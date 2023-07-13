class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        self.answer = 0
        stack = [[(-1,-1)] for _ in range(cols)]
        
        def calculate(row, col, val):
            while stack[col][-1][0] > val:
                height, index = stack[col].pop()
                width = row - stack[col][-1][1] - 1
                self.answer = max(self.answer, height * width)            
            stack[col].append((val,row)) 
                
        for row in range(rows):
            runSum = 0
            for col in range(cols):
                matrix[row][col] = int(matrix[row][col])
                if matrix[row][col] == 0:
                    runSum = 0
                runSum += matrix[row][col]
                matrix[row][col] = runSum
                calculate(row, col, runSum)
        for i in range(cols):
            calculate(rows,i,0)
                
        return self.answer
    
#     [["1","0","1","0","0"],
#      ["1","0","1","1","1"],
#      ["1","1","1","1","1"],
#      ["1","0","0","1","0"]]
                
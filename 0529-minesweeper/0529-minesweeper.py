class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        self.rows = len(board)
        self.cols = len(board[0])
        
        def inbound(row, col):
            if not (-1 < row < self.rows) or not (-1 < col < self.cols):
                return False
            return True
        
        def solution(row, col):
            
            if not inbound(row, col): return 0
            
            val = board[row][col]
            
            if val == "B" or type(val) == int: return 0
            
            elif val == "X": return 1
            
            elif val == "M":
                board[row][col] = "X"
                return 1
            
            board[row][col] = "B"
            
            directions = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1), (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]
            
            mineCount = 0
            for nextRow, nextCol in directions:
                if inbound(nextRow, nextCol) and board[nextRow][nextCol] == "M":
                    mineCount += 1
                    
            if mineCount > 0:
                board[row][col] = str(mineCount)
                return 0
            
            for nextRow, nextCol in directions:
                solution(nextRow, nextCol)
            return 0
        
        solution(click[0], click[1])
        return board
            

                
            
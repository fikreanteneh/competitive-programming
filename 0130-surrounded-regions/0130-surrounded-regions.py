class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        
        def solution(row, col):
            if (row, col) in self.visited:
                return
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            self.visited.add((row, col))
            try:
                if board[row][col] == "O":
                    board[row][col] = ""
                    for neighbor in neighbors:
                        solution(neighbor[0], neighbor[1])
            except:
                return 
            
            
        
        self.visited = set()
        for i in range(m):
            solution(i, 0)
            solution(i, n-1)
        for i in range(n):
            solution(0, i)
            solution(m-1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"        
            
        return board
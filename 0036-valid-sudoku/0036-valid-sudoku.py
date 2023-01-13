class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            col, row, box = set(), set(), set()
            for j in range(9):
                if  board[i][j] != "." and board[i][j] in row:
                    return False
                row.add(board[i][j])
            for j in range(9):
                if board[j][i] != "." and board[j][i] in col:
                    return False
                col.add(board[j][i])
            r, c = (i // 3) * 3, (i % 3)*3
            for j in range(9):
                x, y = j // 3, j % 3
                if board[r + x ][c + y] != "." and board[r + x ][c + y] in box:
                    return False
                box.add(board[r + x ][c + y]) 
        return True
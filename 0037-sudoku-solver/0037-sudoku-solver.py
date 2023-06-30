class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(lambda: set())
        cols = defaultdict(lambda: set())
        boxes = defaultdict(lambda: set())
        free = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    free.append((row, col))
                    continue
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[(row//3, col//3)].add(board[row][col])   
                
        def solution():
            if not free:
                return True
            row, col = free.pop()
            for num in "123456789":
                if (num not in rows[row]) and (num not in cols[col]) and (num not in boxes[(row//3, col//3)]):
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[(row//3, col//3)].add(num)   
                    board[row][col] = num
                    if solution():
                        return True
                    board[row][col] = ""
                    rows[row].discard(num)
                    cols[col].discard(num)
                    boxes[(row//3, col//3)].discard(num)
            free.append((row, col))
            return False
        solution()
        
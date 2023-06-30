class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        index = (0, board[0].index(0)) if 0 in board[0] else (1,board[1].index(0))
        que = deque( [(tuple(board[0]), tuple(board[1]) , index, 0)])
        visited = { (tuple(board[0]), tuple(board[1])) }
        
        while que:
            row1, row2, index, level = que.pop()
            if row1 == (1,2,3) and row2 == (4,5,0):
                return level
            board = [list(row1), list(row2)]
            direction = [(index[0] + 1, index[1]), (index[0] - 1, index[1]), (index[0], index[1] + 1), (index[0], index[1] - 1)]
            x, y = index
            level += 1
            for i, j in direction:
                try:
                    board[i][j], board[x][y] = board[x][y], board[i][j]
                    nextMove = (tuple(board[0]), tuple(board[1]))
                    if nextMove not in visited and -1 < i < 3 and -1 < j < 3:
                        visited.add(nextMove)
                        que.appendleft((nextMove[0], nextMove[1], (i,j), level))
                    board[i][j], board[x][y] = board[x][y], board[i][j]
                except:
                    continue
        
        return -1
            
            
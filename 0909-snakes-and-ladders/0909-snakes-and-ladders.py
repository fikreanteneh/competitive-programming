class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n*n
        
        def findIndex(curr):
            curr -= 1
            oddness = (curr//n) % 2
            x = n - curr//n - 1
            y = abs( (oddness* (n - 1)) - (curr % n))
            return (x, y)

        que = deque([1])
        level = 0
        board[-1][0] = 0
        
        while que:
            length = len(que)
            for _ in range(length):
                curr = que.popleft()
                if curr == target:
                    return level
                for i in range(curr + 1, (min(curr + 6, target)) + 1):
                    x, y = findIndex(i)
                    if board[x][y] > 0:
                        i = board[x][y]
                    if board[x][y] != 0:
                        que.append(i)
                        board[x][y] = 0
            level += 1
        
        return -1
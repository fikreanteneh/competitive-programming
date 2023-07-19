class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        length = len(word)
        direction = ((-1,0),(1,0), (0,1),(0,-1))
        def inbound(i,j):
            return -1 < i < n and -1 < j < m
        self.visited = set()
        def dfs(node, index):
            x, y = node
            if board[x][y] != word[index]:
                return False
            if index == length - 1:
                return True
            self.visited.add(node)
            for a, b in direction:
                i, j = x + a, y + b
                if inbound(i,j) and (i,j) not in self.visited and dfs((i,j), index + 1):
                    return True
            self.visited.discard(node)
            return False
        
        for i in range(n):
            for j in range(m):
                self.visited = set()
                if dfs((i,j), 0):
                    return True
        return False
            
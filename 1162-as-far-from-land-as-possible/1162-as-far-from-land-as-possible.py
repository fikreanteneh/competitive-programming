class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        que = deque([])
        visited = set()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    que.append((i, j, 0))
                    visited.add((i, j))
        answer = -1 
        while que:
            row, col, pos = que.popleft()
            nextMove = [ (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            
            for nextRow, nextCol in nextMove:
                if -1 < nextRow < n and -1 < nextCol < n and (nextRow, nextCol) not in visited:
                    visited.add((nextRow, nextCol))
                    answer = pos + 1
                    que.append((nextRow, nextCol, pos + 1))
        return answer
                    
            
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            row.insert(0, -1)
            row.append(-1)
        n, m = len(grid) + 2, len(grid[0]) 
        grid.insert(0, [-1] * m)
        grid.append([-1] * m)
        
        start, end = None, None
        nonObstacles = 0
        for i in range(1, n -1):
            for j in range(1, m-1):
                if grid[i][j] == 1:
                    start = (i, j)
                    grid[i][j] = 0
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    nonObstacles += 1
        nonObstacles += 1
        self.answer = 0
        def solution(pos, distance):
            if pos == end:
                if distance == nonObstacles:
                    self.answer += 1
                return
            row, col = pos
            grid[row][col] = -1
            direction = [(row + 1, col), (row - 1, col),(row, col + 1),(row, col - 1)]
            for dx in direction:
                if grid[dx[0]][dx[1]] in (0, 2):
                    solution(dx, distance + 1)
            grid[row][col] = 0
                
        solution(start, 0)
        return self.answer
            
            
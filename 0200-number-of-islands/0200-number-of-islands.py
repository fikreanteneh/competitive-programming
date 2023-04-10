class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid) + 2 , len(grid[0]) + 2
        for i in grid:
            i.insert(0,0)
            i.append(0)
        grid.insert(0, [0] * m)
        grid.append([0] * m)
        
        self.answer = 0
        
        def solution(row, col):
            dix = [(row + 1, col), (row -1, col), (row, col + 1), (row, col - 1)]
            grid[row][col] = 0
            for x, y in dix:
                if grid[x][y] == "1":
                    solution(x, y)
        
        for i in range(1, n-1):
            for j in range(1, m-1):
                if grid[i][j] == "1":
                    area = solution(i,j)
                    self.answer  += 1
        return self.answer
        
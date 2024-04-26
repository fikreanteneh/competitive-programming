class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, n):
            grid[i][0] += grid[i -1][0]
            
        for row in range(1, n):
            for col in range(1, m):
                grid[row][col] += min( grid[row - 1][col], grid[row][col - 1])
        
        return grid[-1][-1]
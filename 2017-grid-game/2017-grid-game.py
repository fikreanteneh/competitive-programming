class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sums1 = sums2 = 0
        n = len(grid[0])
        grid[1].append(0)
        grid[0].append(0)
        
        for i in range(n):
            
            #suffix for upper grid
            sums1 += grid[0][n-i-1]
            grid[0][n-i-1] = sums1
            
            #prefix for lower grid
            sums2 += grid[1][i]
            grid[1][i] = sums2
            
        for i in range(n):        
            if grid[0][i+1] < grid[1][i]:
                upper = grid[0][i+1]
                lower = grid[1][i-1]
                return max(upper, lower)
        
        
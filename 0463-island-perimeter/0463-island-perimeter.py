class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.insert(0, 0)
            i.append(0)
        grid.insert(0, [0] * (len(grid[0]) ))
        grid.append([0] * (len(grid[0]) ))
        
        perimeter = 0
        
        for i in range(1,len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j]:
                    perimeter += (1 - grid[i-1][j])
                    perimeter += (1- grid[i+1][j])
                    perimeter += (1 - grid[i][j-1])
                    perimeter += ( 1- grid[i][j + 1])
        return perimeter
    
            
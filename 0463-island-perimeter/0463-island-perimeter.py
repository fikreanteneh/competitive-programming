class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.insert(0, 0)
            i.append(0)
        grid.insert(0, [0] * (len(grid[0]) ))
        grid.append([0] * (len(grid[0]) ))
        bound =[0] #{1:0, 2:0, 3:0, 4:0}
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.calculator(grid, i, j, bound)
        
        return bound[0]
        
        
        
        
    def calculator(self, grid, i, j, bound):
        if not grid[i-1][j]:
            bound[0] += 1
        if not grid[i+1][j]:
            bound[0] += 1
        if not grid[i][j-1]:
            bound[0] += 1
        if not grid[i][j + 1]:
            bound[0] += 1
            
            
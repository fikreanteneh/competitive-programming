class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def surround(grid):
            n, m = len(grid) + 2 , len(grid[0]) + 2
            for i in grid:
                i.insert(0,0)
                i.append(0)
            grid.insert(0, [0] * m)
            grid.append([0] * m)
            return [n, m]
        n, m = surround(grid1)
        surround(grid2)
        
        def solution(row, col):
            curr = 1
            dix = [(row + 1, col), (row -1, col), (row, col + 1), (row, col - 1)]
            grid2[row][col] = 0
            self.positions.add((row,col))
            for x, y in dix:
                if grid2[x][y]:
                    solution(x, y)
        total = 0
        for i in range(1, n-1):
            for j in range(1, m-1):
                if grid2[i][j]:
                    self.positions = set()
                    solution(i,j)
                    
                    for row, col in self.positions:
                        if grid1[row][col] == 0:
                            total -= 1
                            break
                    total += 1
        return total
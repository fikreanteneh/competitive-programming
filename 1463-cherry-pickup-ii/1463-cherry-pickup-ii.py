class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        
        @cache
        def solve(row, col1, col2):
            if row == n:
                return 0
            if col1 == col2:
                return float("-inf")
            
            solutions = []
            for nextCol1 in range(col1 - 1, col1 + 2):
                for nextCol2 in range(col2 - 1, col2 + 2):
                    if not (0 <= nextCol1 < m and 0 <= nextCol2 < m):
                        continue
                    solutions.append(solve(row + 1, nextCol1, nextCol2))
            
            return grid[row][col1] + grid[row][col2] + max(solutions)
        
        return solve(0, 0, m - 1)
                    
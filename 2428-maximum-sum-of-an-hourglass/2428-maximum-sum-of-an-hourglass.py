class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        """
        1 2
        """
        # grid = ([0] * len(grid[0])) + grid
        # sums = sum(grid[0][0:3]) + grid[1][1] + sum(grid[2][0:3])
        # maximum = sums
        sums = maximum = 0
        for i in range(0, len(grid)-2):
            sums = (sum(grid[i][0:3]) + grid[i+1][1] + sum(grid[i+2][0:3]))
            maximum = max(maximum, sums)
            for j in range(0,len(grid[0])- 3):
                sums -= (grid[i][j] + grid[i+2][j] + grid[i + 1][j + 1])
                sums += (grid[i][j+3] + grid[i+2][j+3] + grid[i + 1][j + 2]) 
                maximum = max(maximum, sums)
        return maximum
        """
        1 2 3
        1 4 6
        3 5 7
        """
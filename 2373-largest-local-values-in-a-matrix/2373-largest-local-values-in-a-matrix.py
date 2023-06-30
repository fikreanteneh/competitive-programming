class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [ [] for i in range(n - 2)]
        for y in range(n - 2):
            for x in range(n - 2):
                maxi = 0
                for i in range(y, y+3):
                    for j in range(x, x+3):
                        maxi = max(maxi, grid[i][j])
                ans[y].append(maxi)
        return ans

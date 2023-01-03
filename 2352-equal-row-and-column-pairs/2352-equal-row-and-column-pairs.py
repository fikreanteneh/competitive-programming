class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        # for i in range(n):
        #     flag = True
        #     for j in range(n):
        #         print(grid[i][j], grid[j][i])
        #         if grid[i][j] != grid[j][i]:
        #             flag = False
        #             # break
        #     if flag: 
        #         count += 1
        # return count
        columns = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(grid[j][i])
            columns.append(temp)
        for i in grid:
            for j in columns:
                if i == j:
                    count += 1
        return count
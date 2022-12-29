class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = []
        columns = []
        for i in grid:
            count = dict(Counter(i))
            rows.append((count.get(0, 0), count.get(1, 0)))
        for i in range(len(grid[0])):
            colum = [j[i] for j in grid ]
            count = dict(Counter(colum))
            columns.append((count.get(0, 0), count.get(1, 0)))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = rows[i][1] + columns[j][1] - rows[i][0] - columns[j][0]
        return grid
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1
        target = (n - 1, m - 1)
        stack = deque([((0, 0), 1)])
        visited = set([(0,0)])
        while stack:
            pos, level = stack.pop()
            if pos == target:
                return level
            x, y = pos
            directions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1)]
            for dx in directions:
                try:
                    if dx not in visited and dx[0] > -1 and dx[1] > -1 and grid[dx[0]][dx[1]] == 0:
                        visited.add(dx)
                        stack.appendleft((dx, level + 1))
                except:
                    continue
        return -1
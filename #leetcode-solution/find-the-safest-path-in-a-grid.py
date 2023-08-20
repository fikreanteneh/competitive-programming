class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        que = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    que.append((i,j))
        
        
        level = 0
        visited = set(que)
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def appender(r, c):
            for x, y in direction:
                row, col = r + x, c + y
                if 0 <= row < n and 0 <= col < n and (row, col) not in visited:
                    que.appendleft((row, col))
                    visited.add((row, col))
        
        while que:
            length = len(que)
            for _ in range(length):
                a, b = que.pop()
                grid[a][b] = level
                appender(a,b)
            level += 1
            
        visited = set([(0,0)])
        heap = [(-1 * grid[0][0], 0, 0)]
        answer = float("-inf")
        while heap:
            safeness, r, c = heappop(heap)
            answer = max(safeness, answer)
            for x, y in direction:
                row, col = r + x, c + y
                if row ==col == n - 1:
                    answer = max(answer, -1 * grid[row][col])
                    heap = []
                    break
                if 0 <= row < n and 0 <= col < n and (row, col) not in visited:
                    heappush(heap, (-1 * grid[row][col], row, col))
                    visited.add((row, col))
        return -1 * answer
        
        
        
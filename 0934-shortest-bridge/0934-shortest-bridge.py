class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        group = self.find(grid)
        que = deque(list(group))
        n = len(grid)
        level = 0
        while que:
            length = len(que)
            for _ in range(length):
                node = que.popleft()
                p, q = node
                directions = ( (p + 1, q), (p - 1, q), (p, q+ 1), (p, q - 1) )
                for dx in directions:
                    x, y = dx
                    if not( -1 < x < n ) or not( -1 < y < n) or dx in group:
                        continue
                    if grid[x][y]:
                        return level
                    group.add(dx)
                    que.append(dx)
            level += 1
                
        
        
    
    def find(self,grid):
        n = len(grid)
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    visited.add((i,j))
                    que = deque([(i, j)])
                    while que:
                        p, q = que.popleft()
                        directions = ( (p + 1, q), (p - 1, q), (p, q+ 1), (p, q - 1) )
                        for dx in directions:
                            x, y = dx
                            if -1 < x < n and -1 < y < n and grid[x][y] and (x,y) not in visited:
                                visited.add((x,y))
                                que.append(dx)
                            
                    return visited
        
        
        
                                
                                
                
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        que = deque([]) # row col keys
        visited = set([])
        target = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    que.append( ((i,j), ()) )
                    visited.add(((i,j), ()))
                    
                if grid[i][j].isalpha() and grid[i][j].islower():
                    target += 1
        
        print(target)
        level = 0
        
        def helper(row, col, keys):
            ans = len(keys)
            if not( -1 < row < n ) or not( -1 < col < m):
                return ans
            if grid[row][col] == "#" or ((row, col), keys) in visited:
                return ans
            if grid[row][col].isalpha():
                if grid[row][col].isupper() and grid[row][col] not in keys:
                    return ans
                elif grid[row][col].islower() and grid[row][col].upper() not in keys:
                    keys = tuple(sorted(keys + tuple(grid[row][col].upper())))
            
            visited.add(((row, col), keys))
            que.appendleft(((row, col), keys))
            return len(keys)
        
        while que:
            length = len(que)
            # print(que)
            for _ in range(length):
                node, keys = que.pop()
                p, q = node
                directions = ( (p + 1, q), (p - 1, q), (p, q+ 1), (p, q - 1) )
                for dx in directions:
                    x, y = dx
                    # print( ((x, y), keys), ((x, y), keys) in visited, visited)
                    if helper(x, y, keys) == target:
                        return level + 1
            level += 1
        return -1
                
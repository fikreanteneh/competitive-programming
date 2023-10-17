class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for row in grid: row.append(0)
        grid.append([0]*(n+1))
        parents = [ [(j, i) for i in range(n)]  for j in range(n)]
        rank = [ [1 for _ in range(n)]  for _ in range(n)]
        def find(node):
            row, col = node
            while parents[row][col] != (row, col):
                row, col = parents[row][col]
            rowX, colX = node
            while parents[rowX][colX] != (row, col):
                nextt = parents[rowX][colX]
                parents[rowX][colX] = (row, col)
                rowX, colX = nextt
            return (row, col)
        
        def union(node1, node2):
            row1, col1 = find(node1)
            row2, col2 = find(node2)
            if row1 == row2 and col1 == col2:
                return
            if rank[row2][col2] > rank[row1][row2]:
                node1, node2 = node1, node2
                row1, col1, row2, col2 = row2, col2, row1, col1
            parents[row2][col2] = (row1, col1)
            rank[row1][col1] += rank[row2][col2]
        
        directions = [(0,1),(1, 0),(0,-1),(-1, 0) ]
        def connect(i, j):
           for x, y in directions:
                if grid[i + x][j + y]:
                    union( (i, j), (i + x, j + y))
        
        def calculate(i, j):
            store = {}
            for x, y in directions:
                if grid[i + x][j + y]:
                    area = find( (i + x, j + y) )
                    store[area] = rank[area[0]][area[1]]
            return sum(store.values()) + 1
                              
                    
                              
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                connect(i, j)
        answer = 0
        for i in range(n):
            for j in range(n):
                x, y = find((i,j))
                answer = max(answer, rank[x][y])
                if grid[i][j] == 1:
                    continue
                answer = max(answer, calculate(i, j))
        return answer
                
                
                    
                    
            
                
            
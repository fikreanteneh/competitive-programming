class Solution:
    def latestDayToCross(self, rows: int, cols: int, cells: List[List[int]]) -> int:
        
        parent = [[-1]*cols for _ in range(rows)]
        rank = [[1]*cols for _ in range(rows)]
        
        def find(row, col):
            r, c = row, col            
            while (row,col) != parent[row][col]:
                row, col = parent[row][col]
                if (row, col) in ((-1,-1), (cols,cols)):
                    return (row, col)

            while (r, c) != parent[r][c]:
                    (x, y) = parent[r][c]
                    parent[r][c] = (row, col)
                    r,c = x, y
            return (row,col)
        
        def union(r1, c1, r2, c2):
            p1Row, p1Col = find(r1, c1)
            p2Row, p2Col = find(r2, c2)
            if sorted([p1Row,p1Col, p2Row, p2Col]) == [-1, -1, cols, cols]:
                return True
            if (p1Row, p1Col) == (p2Row, p2Col) :
                return
            
            if (p1Row, p1Col) in ((-1,-1), (cols, cols)):
                parent[p2Row][p2Col] = (p1Row, p1Col)
                return
            
            elif (p2Row, p2Col) in ((-1,-1), (cols, cols)):
                parent[p1Row][p1Col] = (p2Row, p2Col)
                return
            
            if rank[p1Row][p1Col] < rank[p2Row][p2Col]:
                p1Row, p2Row = p2Row, p1Row
                p1Col, p2Col = p2Col, p1Col
            rank[p1Row][p1Col] += rank[p2Row][p2Col]
            parent[p2Row][p2Col] = (p1Row, p1Col)
            
        directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1),(-1,1), (-1,-1)]
        def inbound(r, c):
            return -1 < r < rows and -1 < c < cols
        
        def flood(row, col):
            if col == 0:
                parent[row][col] = (-1, -1)
            elif col == cols - 1:
                parent[row][col] = (cols, cols)
            elif parent[row][col] == -1:
                parent[row][col] = (row, col)
        for day, cell in enumerate(cells):
            cell[0] -=1
            cell[1] -= 1
            flood(cell[0], cell[1])           
            for dx in directions:
                x, y = cell[0] + dx[0], cell[1] + dx[1]
                if inbound(x, y) and parent[x][y] != -1:
                    if union(cell[0], cell[1], x, y):
                        return day
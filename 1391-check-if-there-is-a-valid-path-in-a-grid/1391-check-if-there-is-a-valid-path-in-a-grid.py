class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        paths = [{},
                 {"right": {1,3,5}, "bottom": {}},
                 {"right":{}, "bottom":{2,5,6}},
                 {"right": {}, "bottom": {5,6,2}},
                 {"right":{1,3,5}, "bottom":{2,5,6}},
                 {"right":{}, "bottom":{}}, 
                 {"right":{1,3,5}, "bottom":{}}
                ]
        
        n, m = len(grid), len(grid[0])
        parents, rank = {}, {}
        edges = []
        for i in range(n):
            for j in range(m):
                if i + 1 < n:
                    n0, n1 = grid[i][j], grid[i + 1][j]
                    if n1 in paths[n0]["bottom"]:
                        edges.append(((i,j), (i+1, j)))
                if j + 1 < m:
                    n0, n1 = grid[i][j], grid[i][j + 1]
                    if n1 in paths[n0]["right"]:
                        edges.append(((i,j), (i, j+1)))
                parents[(i,j)] = (i, j)
                rank[(i,j)] = 0
        def find(parent):
            if parent != parents[parent]:
                parents[parent] = find(parents[parent])
            return parents[parent]
        # print(edges)
        def union(p1, p2):
            u1 = find(p1) 
            u2 = find(p2)
            big, small= (u1, u2) if rank[u1] >= rank[u2] else (u2, u1)
            parents[small] = big
            rank[big] += rank[small]
            
        for e1, e2 in edges:
            union(e1, e2)
            
        return find((0,0)) == find((n-1, m-1))
                    
                    
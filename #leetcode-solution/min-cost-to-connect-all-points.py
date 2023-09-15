class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        for i in range(n):
            x0, y0 = points[i]
            for j in range(i + 1, n):
                x1, y1 = points[j]
                edges.append(( abs(x1-x0) + abs(y1-y0), i, j))
                
        def find(node):
            temp = node
            while node != self.parent[node]:
                node = self.parent[node]
                
            while temp != self.parent[temp]:
                x = self.parent[temp]
                self.parent[temp] = node
                temp = x
            return node

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return
            if self.rank[p1] < self.rank[p2]:
                p1, p2 = p2, p1
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
           
        heapify(edges)
        answer = 0
        while edges:
            cost, x, y = heappop(edges)
            if find(x) == find(y):
                continue
            union(x, y)
            answer += cost
        return answer


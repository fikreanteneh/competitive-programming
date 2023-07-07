class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        parent = [i for i in range(n + 1)]
        rank = [1 for i in range(n + 1)]
        cost = [float("inf") for i in range(n + 1)]
        
        def find(node):
            temp = node
            while node != parent[node]:
                node = parent[node]
                
            while temp != parent[temp]:
                x = parent[temp]
                
                parent[temp] = node
                temp = x
            return node

        def union(edge):
            n1, n2, c = edge
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                cost[p1] = min(cost[p1], c, cost[p2])
                return
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            rank[p1] += rank[p2]
            parent[p2] = p1
            cost[p1] = min(cost[p1], c, cost[p2])
        
        for edge in roads:
            union(edge)
        
        parent1 = find(1)
        parent2 = find(n)
        return cost[parent1]
        
        
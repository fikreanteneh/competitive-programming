class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = [i for i in range(len(stones))]
        rank = [1 for i in range(len(stones))]
        
        def find(node):
            temp = node
            while node != parent[node]:
                node = parent[node]
                
            while temp != parent[temp]:
                parent[temp], temp = node, parent[temp]
                # x = parent[temp]
                # parent[temp] = node
                # temp = x
            return node

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            rank[p1] += rank[p2]
            parent[p2] = p1
            
        for i in range(0, len(stones)):
            x0, y0 = stones[i]
            for j in range(i+1, len(stones)):
                x1, y1 = stones[j]
                if x1 == x0 or y1 == y0:
                    union(i, j)
        
        for i in range(len(stones)):
            find(i)
            
        return len(stones) - len(set(parent))
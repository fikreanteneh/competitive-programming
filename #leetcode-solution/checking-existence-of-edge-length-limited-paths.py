class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        for i, query in enumerate(queries):
            query.append(i)
        edgeList.sort(key = lambda x: x[2])
        queries.sort(key = lambda x: x[2])
        
        parent = [i for i in range(n)] 
        rank = [1] * n
        costs = [float("inf")] * n
        
        def find(node):
            temp = node
            while node != parent[node]:
                node = parent[node]
                
            while temp != parent[temp]:
                x = parent[temp]
                parent[temp] = node
                temp = x
            return node
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1

            rank[p1] += rank[p2]
            parent[p2] = p1
        
        edgeLen = len(edgeList)
        queryLen = len(queries)
        curr = 0
        answer = [False] * queryLen
        for start, end, distance, index in queries:
            while curr < edgeLen and edgeList[curr][2] < distance:
                edge = edgeList[curr]
                a, b, cost = edge
                union(a, b)
                p = find(a)
                costs[p] = max(costs[p], cost) 
                curr += 1
            answer[index] = find(start) == find(end)
        return answer

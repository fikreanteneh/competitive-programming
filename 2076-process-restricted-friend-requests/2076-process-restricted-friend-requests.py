class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        restricted = {i: [set(), set([i])] for i in range(n)}
        for restriction in restrictions:
            restricted[restriction[0]][0].add(restriction[1])
            restricted[restriction[1]][0].add(restriction[0])
            
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
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
            n1, n2 = edge
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return True
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
                
            if restricted[p2][1].intersection(restricted[p1][0]):
                return False
            rank[p1] += rank[p2]
            parent[p2] = p1
            restricted[p1][0].update(restricted[p2][0])
            restricted[p1][1].update(restricted[p2][1])
            return True
        answer = []
        
        for request in requests:
            answer.append(union(request))
        return answer




    
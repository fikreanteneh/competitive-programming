class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]
        rank = [0 for i in range(len(edges))]
        
        def parentChild(node):
            stack = []
            while node != parent[node]:
                stack.append(node)
                node = parent[node]
            return (node, stack)
        
        def find(node1, node2):
            p1, child1 = parentChild(node1)
            p2, child2 = parentChild(node2)
            if p1 == p2:
                return True
            big, small, bigC, smallC = (p1, p2, child1, child2) if rank[p1] >= rank[p2] else (p2, p1, child2, child1)
            smallC.append(small)
            rank[big] += len(smallC)
            while smallC:
                x = smallC.pop()
                rank[x] = 0
                parent[x] = big
                
        for x, ede in enumerate(edges):
            i, j = ede[0] - 1, ede[1] - 1
            if find(i,j):
                return ede
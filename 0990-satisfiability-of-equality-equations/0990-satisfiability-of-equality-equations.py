class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        parent = [i for i in range(26)]
        rank = [1 for i in range(26)]
        
        def find(node):
            temp = node
            while node != parent[node]:
                node = parent[node] 
            while temp != parent[temp]:
                rank[node] += rank[temp]
                rank[temp] = 0
                temp, parent[temp] = parent[temp], node
            
            return node
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            big, small = (p1, p2) if rank[p1] >= rank[p2] else (p2, p1)
            rank[big] += rank[small]
            rank[small] = 0
            parent[small] = big
        
        for equ in equations:
            if equ[1] == "=":
                union(ord(equ[0]) - 97, ord(equ[-1]) - 97)

        for equ in equations:
            x = find(ord(equ[0]) - 97)
            y = find(ord(equ[-1]) - 97)
            
            if (equ[1] == "!" and (x == y)) or (equ[1] == "=" and (x != y)):
                return False
        
        return True
                
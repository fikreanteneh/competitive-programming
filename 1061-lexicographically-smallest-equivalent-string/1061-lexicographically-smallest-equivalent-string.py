class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = [i for i in range(26)]
        rank = [1 for i in range(26)]
        smallest = [i for i in range(26)]
        
        
        def find(node):
            smallest = node
            temp = node
            total = 0
            while node != parent[node]:
                total += rank[node]
                node = parent[node]
                smallest = min(node, smallest)
            rank[node] += total
            while temp != parent[temp]:
                rank[temp] = 0
                temp, parent[temp] = parent[temp], node
            return node
                
        
        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            big, small = (p1, p2) if rank[p1] >= rank[p2] else (p2, p1)
            parent[small] = big
            rank[big] += rank[small]
            smallest[big] = min(smallest[big], smallest[small])
            
            
        for i in range(len(s1)):
            union(ord(s1[i]) - 97, ord(s2[i]) - 97)
        
        
        answer = []
        for i in range(len(baseStr)):
            x = find(ord(baseStr[i])-97)
            answer.append(chr(smallest[x] + 97))
        
        return "".join(answer)
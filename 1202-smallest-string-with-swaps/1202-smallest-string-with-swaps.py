class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]
        rank = [1 for i in range(len(s))]
        
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
            if p1 == p2:
                return
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            rank[p1] += rank[p2]
            parent[p2] = p1
            
        for pair in pairs:
            union(pair[0], pair[1])
        for i in range(len(parent)):
            find(i)
        
        group = defaultdict(lambda: [[],[]])
        for i, j in enumerate(parent):
            group[j][0].append(i)
            group[j][1].append(s[i])
        ans = [""] * len(parent)
        for i, j in group.items():
            index, char = j
            char.sort()
            for v, ind in enumerate(index):
                ans[ind] = char[v]
        return "".join(ans)
                
        

        
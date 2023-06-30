class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        name = defaultdict(str)
        rank = defaultdict(lambda: 1)
        
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
            
        for acc in accounts:
            name[acc[1]] = acc[0]
            if acc[1] not in parent:
                parent[acc[1]] = acc[1]
            
            for i in range(2, len(acc)):
                name[acc[i]] = acc[0]
                if acc[i] not in parent:
                    parent[acc[i]] = acc[i]
                union(acc[1], acc[i])
        for i in parent:
            find(i)
        
        group = defaultdict(list)
        
        for i, j in parent.items():
            if j not in group:
                group[j].append(name[j])
            group[j].append(i)
        ans = []
        for i in group.values():
            ans.append([i[0]] + sorted(i[1:]))
        return ans

        
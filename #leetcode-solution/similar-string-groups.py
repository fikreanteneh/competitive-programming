class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
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
        for i, word in enumerate(strs):
            for j in range(i + 1, n):
                mismatch = 0
                for x, y in zip(word, strs[j]):
                    if x != y:
                        mismatch += 1
                if mismatch <= 2:
                    union(i, j)
        answer = set()
        for i in range(n):
            answer.add( find(i) )
        return len(answer)
        
        
            
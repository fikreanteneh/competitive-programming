class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        group = [defaultdict(int) for i in range(n)]
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
        
        for allowed in allowedSwaps:
            union(allowed[0], allowed[1])
        answer = 0
        for i, val in enumerate(source):
            par = find(i)
            group[par][val] += 1
        for i in range(n):
            sour = group[parent[i]]
            tar = target[i]
            if sour[tar]:
                sour[tar] -= 1
            else:
                answer += 1
        return answer
        
        
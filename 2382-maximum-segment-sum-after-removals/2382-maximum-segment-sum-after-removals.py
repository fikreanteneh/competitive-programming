class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = [-1] * ( n + 1)
        rank = [0] * n
        answer = [0]
        self.last = 0
        
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
            nums[p1] += nums[p2]
            parent[p2] = p1
        
        for query in reversed(removeQueries):
            parent[query] = query
            rank[query] = 1
            if parent[query + 1] != -1:
                union(query, query + 1)
            if parent[query - 1] != -1:
                union(query, query - 1)
            find(query)
            self.last = max(self.last, nums[parent[query]])
            answer.append(self.last)
        answer.pop()
        answer.reverse()
        return answer
            

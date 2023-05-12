class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = {i:[0 ,[]] for i in range(n)}
        for i, j in edges:
            graph[i][1].append(j)
            graph[j][0] += 1
        
        answer = [set() for _ in range(n)] 
        que = deque([])
        for i,neigh in graph.items():
            if neigh[0] == 0:
                que.append(i)
        
        def helper(parent, child):
            for i in parent:
                child.add(i)
        
        while que:
            node = que.pop()    
            
            for child in graph[node][1]:
                answer[child].add(node)
                helper(answer[node], answer[child])
                graph[child][0] -= 1
                if graph[child][0] == 0:
                    que.append(child)
        for i, val in enumerate(answer):
            answer[i] = sorted(list(val))
        return answer
        
            
            
            
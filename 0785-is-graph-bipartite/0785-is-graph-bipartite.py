class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
            
        n = len(graph)

        
        group = [-1] * n
        
        def solution(node, g):
            if group[node] not in (g, -1):
                return False
            
            group[node] = g
            
            for i in graph[node]:
                if group[i] != -1 and group[i] != group[node]:
                    continue
                if not solution(i, 1 - g):
                    return False
            return True
        
        for i in range(n):
            if group[i] == -1:
                if not solution(i, 0):
                    return False
        return True
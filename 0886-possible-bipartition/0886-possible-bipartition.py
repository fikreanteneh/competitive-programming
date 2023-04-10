class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        
        for i,j in dislikes:
            graph[i - 1].append(j - 1)
            graph[j - 1].append(i - 1)

        
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
        
        for i in graph:
            if group[i] == -1:
                if not solution(i, 0):
                    return False
        return True
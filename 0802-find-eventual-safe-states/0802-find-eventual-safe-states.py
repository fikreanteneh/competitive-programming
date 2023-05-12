class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        answer = []
        visited = set()
        def solution(node, visited):
            if node in visited:
                return False
            if graph[node] in (True, False):
                return graph[node]
            visited.add(node)
            flag = True
            for child in graph[node]:
                flag = flag and solution(child, visited)
            visited.discard(node)   
            if flag:
                answer.append(node)
                graph[node] = True
                return True
            graph[node] = False
            return False
        
        
        for node in range(len(graph)):
            if graph[node] not in (False, True): 
                solution(node, set())
        answer.sort()
        return answer
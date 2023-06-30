class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[pre].append(course)
        answer = []
        visited = set()
        def solution(node, visited):
            if node in visited:
                return True
            visited.add(node)
            for child in graph[node]:
                if graph[child] != None and solution(child, visited):
                    return True
            
            answer.append(node)
            graph[node] = None
        
        
        for node in range(numCourses):
            if graph[node] != None and solution(node, set()):
                return False
        return True
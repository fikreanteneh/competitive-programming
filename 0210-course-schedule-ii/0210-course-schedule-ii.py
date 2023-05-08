class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {i: [0, []] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course][0] += 1
            graph[pre][1].append(course)
        answer = []
        visited = set()
        def solution(node, visited):
            if node in visited:
                return True
            visited.add(node)
            for child in graph[node][1]:
                if graph[child] and solution(child, visited):
                    return True
            
            answer.append(node)
            graph[node] = None
        
        
        for node in range(numCourses):
            if graph[node] and solution(node, set()):
                return []
        answer.reverse()
        return answer
        
        # graph = {i: [0, []] for i in range(numCourses)}
        # for course, pre in prerequisites:
        #     graph[course][0] += 1
        #     graph[pre][1].append(course)
        # answer = []
        # que = deque([])
        # for node, val in graph.items():
        #     if not val[0]:
        #         que.append(node)
        # while que:
        #     node = que.pop()
        #     answer.append(node)
        #     for child in graph[node][1]:
        #         graph[child][0] -= 1
        #         if graph[child][0] == 0:
        #             que.appendleft(child)    
        # if len(answer) != numCourses:
        #     return []
        # return answer
            
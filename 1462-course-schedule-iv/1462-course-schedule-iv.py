class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i: [0, []] for i in range(numCourses)}
        preq = {i: set([i]) for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course][0] += 1
            graph[pre][1].append(course)
        que = deque([])
        for node, val in graph.items():
            if not val[0]:
                que.append(node)
        while que:
            node = que.pop()
            for child in graph[node][1]:
                # print(pre[child], pre[node])
                preq[child].update(preq[node])
                graph[child][0] -= 1
                if graph[child][0] == 0:
                    que.appendleft(child)    
        answer = []
        # print(preq)
        for i in queries:
            answer.append(i[1] in preq[i[0]])
        return answer
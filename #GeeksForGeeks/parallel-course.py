from collections import deque
def parallelCourses(n, prerequisites):
    # Write your code here.

    graph = [[[], 0] for _ in range(n)]
    for before, after in prerequisites:
        graph[before - 1][0].append(after - 1)
        graph[after - 1][1] += 1
    que = deque([])
    for i, (child, incoming) in enumerate(graph):
        if incoming == 0:
            que.append(i)
    answer = 0
    while que:
        length = len(que)
        for _ in range(length):
            node = que.pop()
            for child in graph[node][0]:
                graph[child][1] -= 1
                if graph[child][1] == 0:
                    que.appendleft(child)
        answer += 1
    for child, incoming in graph:
        if incoming:
            return -1
    return answer

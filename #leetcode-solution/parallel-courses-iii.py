class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:    
        graph = [[[], 0, 0] for _ in range(n)]
        for before, after in relations:
            graph[before - 1][0].append(after - 1)
            graph[after - 1][1] += 1
        que = deque([])
        for i, (child, incoming, _) in enumerate(graph):
            if incoming == 0:
                que.append(i)
        answer = 0
        while que:
            length = len(que)
            for _ in range(length):
                node = que.pop()
                mine = graph[node][2] + time[node]
                if len(graph[node][0]) == 0:
                    answer = max(answer, mine)
                for child in graph[node][0]:
                    graph[child][1] -= 1
                    graph[child][2] = max(mine, graph[child][2])
                    if graph[child][1] == 0:
                        que.appendleft(child)
        return answer
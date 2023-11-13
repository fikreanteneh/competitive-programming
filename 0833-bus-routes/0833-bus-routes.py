class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            n = len(route)
            for j in range(n):
                graph[route[j]].append(i)
        visited = set(graph[source])
        que = deque(graph[source])
        level = 0
        while que:
            level += 1
            n = len(que)
            for _ in range(n):
                bus = que.pop()
                for stop in routes[bus]:
                    if stop == target:
                        return level 
                    for nextBus in graph[stop]:
                        if nextBus not in visited:
                            que.appendleft(nextBus)
                            visited.add(nextBus)
        return -1

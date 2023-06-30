class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph = defaultdict(list)
        for i, val in enumerate(routes):
            n = len(val)
            for j in range(n):
                graph[val[j]].append( (i,val[(j + 1)%n]) )
        visited = set([(source, -1)])
        route = deque([(source, 0, -1)])
        while route:
            pos, level, cur = route.pop()
            if pos == target:
                return level
            visited.add((pos,cur))
            level += 1
            for bus, forward in graph[pos]:
                if (forward, bus) not in visited:
                    if bus == cur:
                        route.append((forward, level - 1, bus))
                    else:
                        route.appendleft((forward, level, bus))
                        
        return -1
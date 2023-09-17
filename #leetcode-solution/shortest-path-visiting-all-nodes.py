class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        
        target = (1 << n) - 1
        visited = set([(i, 1 << i) for i in range(n)])
        que = deque([(i, 1 << i) for i in range(n)])
        level = 0
        while que:
            length = len(que)
            for _ in range(length):
                node, path = que.popleft()
                if path == target:
                    return level
                for child in graph[node]:
                    nextPath = path | 1 << child
                    if (child, nextPath) not in visited:
                        visited.add((child, nextPath))
                        que.append((child, nextPath))
            level += 1
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(lambda : set())
        for i in edges:
            graph[i[0]].add(i[1])
            graph[i[1]].add(i[0])
        stack = [source]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            elif node == destination:
                return True
            visited.add(node)
            for i in graph[node]:
                stack.append(i)
        return False
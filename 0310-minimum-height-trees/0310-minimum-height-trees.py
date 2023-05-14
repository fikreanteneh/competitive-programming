class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [i for i in range(n)]
        graph = defaultdict(lambda: set())
        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)

        que = deque([])
        for node, child in graph.items():
            if len(child) == 1:
                que.append(node)
        while que:
            length = len(que)
            if length == len(graph):
                return list(que)
            for _ in range(length):
                curr = que.pop()
                for child in graph[curr]:
                    graph[child].discard(curr)
                    if len(graph[child]) == 1:
                        que.appendleft(child)
                graph.pop(curr)
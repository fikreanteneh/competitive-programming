class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for edge, prob in zip(edges, succProb):
            x, y = edge
            graph[x].append((prob, y))
            graph[y].append((prob, x))
            
        probability = [0] * n
        heap = [ (-1, start_node)]
        visited = set()
        while heap:
            prob, node = heappop(heap)
            if node in visited:
                continue
            probability[node] = -1 * prob
            visited.add(node)
            for probab, child in graph[node]:
                if child not in visited:
                    heappush( heap,( prob*probab, child) )
        return probability[end_node]
            
            
        
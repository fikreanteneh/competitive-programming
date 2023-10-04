class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [float("inf")] * n
        visited = set()
        graph = [ [] for _ in range(n)]
        for start, end, cost in times:
            graph[start - 1].append((end - 1, cost))
        heap = [(0, k - 1)]
        while heap:
            cost, node = heappop(heap)
            if node in visited:
                continue
            distance[node] = cost
            visited.add(node)
            for nextNode, nextCost in graph[node]:
                heappush(heap,(nextCost + cost, nextNode))
        if float("inf") in distance:
            return -1
        return max(distance)
        
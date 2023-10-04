class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # k += 1
        # distance = [float("inf")] * n
        # visited = set()
        # graph = [ [] for _ in range(n)]
        # for start, end, cost in flights:
        #     graph[start].append((end, cost))
        # heap = [(0, src, 0)]
        # while heap:
        #     cost, node, level = heappop(heap)
        #     if (node, level) in visited:
        #         continue
        #     distance[node] = cost
        #     if node == dst:
        #         return distance[node]
        #     visited.add( (node, level))
        #     if level == k:
        #         continue
        #     for nextNode, nextCost in graph[node]:
        #         heappush(heap,(nextCost + cost, nextNode, level + 1))
        # if distance[dst]  == float("inf"):
        #     return -1
        # return distance[dst]
        distance = [float("inf")] * n
        distance[src] = 0
        for _ in range(k + 1):
            temp = distance.copy()
            for start, end, cost in flights:
                temp[end] = min(distance[start] + cost, temp[end])         
            distance = temp
        if distance[dst]  == float("inf"):
            return -1
        return distance[dst]
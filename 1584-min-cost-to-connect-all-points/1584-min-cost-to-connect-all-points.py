class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        pq = [(0,0)]
        visited = set()
        heapify(pq)
        ans = 0
        while pq:
            # print(pq)
            cost, node = heappop(pq)
            if node in visited:
                continue
            ans += cost
            visited.add(node)
            for j in range(n):
                # print(node, j)
                distance = abs(points[node][0] - points[j][0]) + abs(points[node][1] - points[j][1])
                heappush(pq, (distance, j))
        return ans
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for fromm, to, cost in edges:
            self.graph[fromm].append((cost, to)) 


    def addEdge(self, edge: List[int]) -> None:
        fromm, to, cost = edge
        self.graph[fromm].append((cost, to)) 
        

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        for cost, dest in self.graph[node1]:
            heap.append( (cost, dest) )
        heapify(heap)
        visited = set()
        while heap:
            cost, node = heappop(heap)
            if node == node2:
                return cost
            if node in visited:
                continue
            visited.add(node)
            for costt, dest in self.graph[node]:
                heappush(heap,  (cost + costt, dest) )
        return -1


        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
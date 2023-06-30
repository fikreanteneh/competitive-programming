class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(lambda : set())
        for i in roads:
            graph[i[0]].add(i[1])
            graph[i[1]].add(i[0])

        done = set()
        maxi = 0
        for i in range(n):
            # total = len(graph[i]) - 1
            for j in range (n):
                if i == j:
                    continue
                # x = len( (graph[i].union(graph[j]) )
                x = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    x -= 1
                maxi = max( x , maxi)
        return maxi
        
        
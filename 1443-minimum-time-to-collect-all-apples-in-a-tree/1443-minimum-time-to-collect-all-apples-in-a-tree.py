class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.graph = defaultdict(list)
        for i,j in edges:
            self.graph[i].append(j)
            self.graph[j].append(i)
        visited = set()
        self.answer = 0
        def dfs(node):
            time = 0
            if node in visited:
                return 0
            visited.add(node)
            for child in self.graph[node]:
                time += dfs(child)
            if hasApple[node] or time:
                time += 2
            # print(node ,">>", time)
            return time
        answer = dfs(0)
        return answer - 2 if answer else 0
            
            
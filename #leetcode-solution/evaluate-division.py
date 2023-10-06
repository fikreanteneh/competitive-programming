class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda: {} )
        for equation, value in zip(equations, values):
            start, end = equation
            graph[end][start] = 1/value
            graph[start][end] = value
            graph[start][start] = 1
            graph[end][end] = 1
        def dfs(node, goal, curr, visited):
            if node == goal:
                return curr
            visited.add(node)
            for child, value in graph[node].items():
                if child in visited:
                    continue
                val = dfs(child, goal, curr * value, visited)
                if val > -1:
                    return val
            return -1.0
        answer = []        
        for x, y in queries:  
            if x not in graph or y not in  graph:
                answer.append(-1.0)
                continue
            ans = dfs(x, y, 1,set())
            answer.append(ans)
        return answer
            
            
            
            
    
    
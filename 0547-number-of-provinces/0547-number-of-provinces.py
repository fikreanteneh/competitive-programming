class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {}
        for i in range(len(isConnected)):
            graph[i] = []
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j]:
                    graph[i].append(j)
        visited = set()           
        self.group = 0 
        self.temp = set()
        def solution(node, parent):
            if node in visited:
                return
            visited.add(node)
            
            if parent not in self.temp:
                self.group += 1
                self.temp = set()
            self.temp.add(node)
            for next in graph[node]:
                solution(next, node)
        
        for i in graph:
            solution(i, None)
        return self.group
        
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowGraph = self.helper2(rowConditions, k)
        colGraph = self.helper2(colConditions, k)
        
        self.helper(rowGraph, k)
        self.helper(colGraph, k)
        answer = [[0] * k for i in range(k)]
        for i in range(1, k + 1):
            row, col = rowGraph[i], colGraph[i]
            if type(row) != int or type(col) != int:
                return []
            answer[row][col] = i
        
        return answer
            

    
    
    def helper(self, graph, k):
        que = deque([])
        for i in range(1, k + 1):
            if graph[i][1] == 0:
                que.append(i)
        
        curr = 0
        while que:
            node = que.popleft()
            for child in graph[node][0]:
                graph[child][1] -= 1
                if graph[child][1] == 0:
                    que.append(child)
            graph[node] = curr
            curr += 1
            
    def helper2(self, arr, k):
        graph = {i:[set(), 0] for i in range(1, k + 1)}
        for row in arr:
            if row[1] not in graph[row[0]][0]:
                graph[row[0]][0].add(row[1])
                graph[row[1]][1] += 1
        return graph
            
            
                
            
        
            
        
        
        
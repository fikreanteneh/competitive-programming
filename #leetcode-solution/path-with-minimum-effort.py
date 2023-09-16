class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        n, m = len(heights), len(heights[0])
        store = [[0 for i in range(m)] for i in range(n)]

            
        for i in range(n):
            heights[i].append(float("inf"))
        heights.append([float("inf")]*(m + 1))
                              
        heap = [(0, 0, 0)]
        visited = {(0,0) : 0}
        while heap:
            cost, row, col = heappop(heap)
            if row == n - 1 and col == m - 1:
                return cost
            direction = [(-1, 0), (0,-1), (1,0),(0,1)]
            
            for x, y in direction:
                newRow, newCol = row + x, col + y
                newCost = max(cost, abs(heights[row][col] - heights[newRow][newCol]))
                if newCost < visited.get((newRow, newCol), float("inf")):
                    visited[(newRow, newCol)] = newCost
                    heappush(heap, (newCost, newRow, newCol))
            
                
            
    
        
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        maxHeap = []
        for i in range(n):
            for j in range(n):
                heappush(maxHeap, -matrix[i][j])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -heappop(maxHeap)
            
        

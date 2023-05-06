class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        n = len(matrix)
        heapify(nums)
        for i, val in enumerate(matrix):
            heappush(nums, (val[0], i, 0))
        
        for i in range(k-1):
            curr, index, index2 = heappop(nums)
            if index2 < n - 1:
                index2 += 1
                heappush(nums, (matrix[index][index2], index, index2))
        return nums[0][0]
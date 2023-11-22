class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        length = 0
        for i, row in enumerate(nums):
            length = max(length, i + len(row) - 1)
        answer = [ [] for _ in range(length + 1)]
        for i, row in enumerate(nums):
            for j, col in enumerate(row):
                answer[i + j].append(col)
        return [ val for row in answer for val in reversed(row) ]       
                  
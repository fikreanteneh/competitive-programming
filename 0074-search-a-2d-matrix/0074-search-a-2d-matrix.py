class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left,right = 0, n - 1
        mid = 0
        while left <= right:
            mid = (right + left) // 2
            if n == mid + 1 or matrix[mid][0] <= target < matrix[mid + 1][0]:
                break
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        if left > right: mid = 0
        values = matrix[mid]
        left, right = 0, m-1
        while left <= right:
            mid = left + ((right - left) // 2)
            if values[mid] == target:
                return True
            elif values[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for index in range(len(matrix[0])):
            row = []
            for index2 in range(len(matrix)):
                row.append(matrix[index2][index])
            result.append(row)
        return result

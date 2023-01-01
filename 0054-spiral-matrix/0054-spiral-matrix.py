class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rltb = [len(matrix[0]) - 1, 0, 0, len(matrix) - 1]
        answer = []
        size = len(matrix) * len(matrix[0])
        return self.right(matrix, rltb, answer, size)
    def right(self, matrix, rltb, answer, size):
        for i in range(rltb[1], rltb[0] + 1):
            answer.append(matrix[rltb[2]][i])
        rltb[0] -= 1
        rltb[2] += 1
        if len(answer) == size:
            return answer
        return self.bottom(matrix, rltb, answer, size)
    def bottom(self, matrix, rltb, answer, size):
        for i in range(rltb[2], rltb[3] + 1):
            answer.append(matrix[i][rltb[0] + 1])
        if len(answer) == size:
            return answer
        return self.left(matrix, rltb, answer, size)
    def left(self, matrix, rltb, answer, size):
        for i in range(rltb[0], rltb[1] - 1, -1):
            answer.append(matrix[rltb[3]][i])
        rltb[1] += 1
        rltb[3] -= 1
        if len(answer) == size:
            return answer
        return self.top(matrix, rltb, answer, size)
    def top(self, matrix, rltb, answer, size):
        for i in range(rltb[3], rltb[2] - 1, -1):
            answer.append(matrix[i][rltb[1] - 1])
        if len(answer) == size:
            return answer
        return self.right(matrix, rltb, answer, size)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        flip = False
        answer = []
        n, m = len(mat) - 1, len(mat[0]) - 1
        if n == 0: return mat[0]
        for i in range((n+1)*(m+1)):

            temp = []
            row, colum = i, 0
            if i > n: 
                row = n
                colum = i - n
            while row >= 0 and colum <= m:
                temp.append(mat[row][colum])
                row -= 1
                colum += 1
            if flip: temp.reverse()
            answer.extend(temp)
            flip = not flip
        return answer
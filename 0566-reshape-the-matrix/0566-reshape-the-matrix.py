class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        if n * m != r * c: 
            return mat
        ans = [ [0] * c for i in range(r) ]
        print(ans)
        for i in range(m * n):
            ans[i//c][i%c] = mat[i//m][i%m]
        return ans
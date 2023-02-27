class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
    
        
        
        matrix = [[0] * (n + 1) for j in range(n + 1)]
        
        for query in queries:
            
            matrix[query[0]] [query[1]]  += 1
            matrix[query[2] + 1] [query[3] + 1]  += 1
            
            matrix[query[0]] [query[3] + 1]  -= 1
            matrix[query[2] + 1] [query[1]]  -= 1
        
        for i in range(n):
            sums = 0
            for j in range(1, n):
                matrix[j][i] +=  matrix[j-1][i]
        
        for i in range(n):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
            matrix[i].pop()
        matrix.pop()
        # print(matrix)
        return  matrix      
            
      
#         for column in matrix:
#             sums = 0
#             for i in range(n):
#                 sums += column[i]
#                 column[i] = sums
#         return matrix
        
        
        # 1 0 -1 0   1 1 0 0
        # 1 1 -1 -1  1 2 1 0
        # 0 1 0 -1   0 1 1 0
        
#         0  0  0  0   0    
#         0  1  0  -1   0   
#         0  0  1  0   -1   0 
#         0 -1  0  0   0
#         0  0 -1  0   0
        
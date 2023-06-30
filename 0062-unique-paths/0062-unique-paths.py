class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        memo[(m-1, n-1)] = 1
        def calc(node):
                if node in memo:
                    return memo[node]
                x, y = node
                if x < m:
                    memo[node] += calc((x + 1, y))
                if y < n:
                    memo[node] += calc((x, y + 1))
                return memo[node]
        
        return calc((0,0))
    
    
        # path = [[0 for i in range(n)] for j in range(m)]
        # path[0][0] = 1
        # for i in range(m):
        #     for j in range(n):
        #         if j > 0:
        #             path[i][j] += path[i][j-1]
        #         if i > 0:
        #             path[i][j] += path[i-1][j]
        #         print(path)
        # return path[m-1][n-1]
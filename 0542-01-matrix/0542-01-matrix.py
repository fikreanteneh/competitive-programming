class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        ans = [[0] * m for i in range(n)]
        que = deque([])
        visited = set()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    que.appendleft(((i, j),0))
                    visited.add((i,j))
        while que:
            index, level = que.pop()
            ans[index[0]][index[1]] = level
            direction = [(index[0] + 1, index[1]), (index[0] - 1, index[1]), (index[0], index[1] + 1), (index[0], index[1] - 1)]
            level += 1
            for i, j in direction:
                try:
                    if (i,j) not in visited and -1 < i < n and -1 < j < m:
                        que.appendleft( ((i,j), level)) 
                        visited.add((i,j))
                        
                except:
                    continue
            
        return ans
            
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n, m = len(dungeon), len(dungeon[0])
        
        store = [ [0 for _ in range(m)] for _ in range(n) ]
        store[n - 1][m - 1] = max(1, 1 - dungeon[n - 1][m - 1])
        
        for i in range(n - 2, -1, -1):
            store[i][-1] = max(1, store[i + 1][-1] - dungeon[i][-1])
        for i in range(m - 2, -1, -1):
            store[-1][i] = max(1, store[-1][ i + 1] - dungeon[-1][i])
            
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                mini = min(store[i + 1][j], store[i][j + 1])
                store[i][j] = max(1, mini - dungeon[i][j])
        
        return store[0][0]
        
        

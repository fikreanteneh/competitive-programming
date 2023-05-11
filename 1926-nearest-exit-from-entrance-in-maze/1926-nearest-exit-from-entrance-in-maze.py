class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)
        n, m = len(maze), len(maze[0])
        
        que = deque([(entrance, 0)])
        
        while que:
            # print(que)
            node, level = que.pop()
            x, y = node
            if node != entrance and (x in (0, n-1) or y in (0, m-1)):
                return level
            level += 1
            maze[x][y] = "+"
            dx = [  (x + 1, y)  , (x - 1, y)  , (x, y + 1)  , (x, y - 1) ]
            for d in dx:
                i, j = d
                try:
                    if i > -1 and j > -1 and maze[i][j] == ".":
                        maze[i][j] = "+"
                        que.appendleft((d, level))
                except:
                    continue
        
        
        return -1
    

        
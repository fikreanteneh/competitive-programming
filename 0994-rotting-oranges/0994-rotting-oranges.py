class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            row.insert(0, 0)
            row.append(0)
        n, m = len(grid) + 2, len(grid[0]) 
        grid.insert(0, [0] * m)
        grid.append([0] * m)
        
        rotten = []
        oranges = 0
        for i in range(1, n -1):
            for j in range(1, m-1):
                if grid[i][j] == 2:
                    rotten.append( ((i, j),0) )
                if grid[i][j]:
                    oranges += 1
        answer = defaultdict(lambda: float("inf"))
        

        self.visited = set()
        fringe = deque(rotten)
        while fringe:
                node, level = fringe.pop()
                if node in self.visited:
                    continue
                self.visited.add(node)
                answer[node] = min(answer[node], level)
                level += 1
                directions = [(node[0] + 1, node[1]), (node[0] - 1, node[1]), (node[0], node[1] + 1), (node[0], node[1] - 1)]
                for dx in directions:
                    if dx not in self.visited and grid[dx[0]][dx[1]] == 1:
                        fringe.appendleft((dx, level))
        if len(answer) != oranges:
            return -1
        if len(answer) == 0:
            return 0
        return max(answer.values())
            

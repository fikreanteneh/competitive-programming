class DetectSquares:

    def __init__(self):
        self.ans = defaultdict(int)
        self.x = defaultdict(lambda: defaultdict(int))
        self.y = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point        
        self.x[x][y] += 1
        self.y[y][y] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        answer  = 0
        for nextY, value in self.x[x].items():
            side = y - nextY
            if side == 0:
                continue
            p1, p2 = self.x[x + side][nextY], self.x[x + side][y] 
            answer += ( p1*p2*value)
            p1, p2 = self.x[x - side][nextY], self.x[x - side][y] 
            answer += ( p1*p2*value)
        return answer
            

# class DetectSquares:

#     def __init__(self):
#         self.ans = defaultdict(int)
#         self.store = defaultdict(int)
#         self.stack = defualtdict(int)
#         self.x = defaultdict(lambda: defaultdict(int))
#         self.y = defaultdict(lambda: defaultdict(int))

#     def add(self, point: List[int]) -> None:
#         x, y = point  
#         for nextX in self.stack:
#             side = x - nextX
            
#         self.x[x][y] += 1
#         self.y[y][y] += 1
        

#     def count(self, point: List[int]) -> int:
#         x, y = point
#         answer  = 0
#         for nextY, value in self.x[x].items():
#             side = y - nextY
#             p1, p2 = self.x[x + side][nextY], self.x[x + side][y] 
#             answer += ( p1*p2*value)
#             p1, p2 = self.x[x - side][nextY], self.x[x - side][y] 
#             answer += ( p1*p2*value)
#         return answer
            
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
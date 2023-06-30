class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        self.visited = set()
        ranges = [ [] for i in range(n)]
        for i, val in enumerate(bombs):
            a, b, r1 = val
            for j,va in enumerate(bombs):
                x, y, r = va
                if r1 ** 2 >= ((a-x) ** 2) + ((b - y) ** 2):
                    ranges[i].append(j)
        
        self.answer = 0
        def solution(node):
            if node in self.temp:
                return
            self.temp.add(node)
            self.visited.add(node)
            for i in ranges[node]:
                solution(i)
            
        for i in range(n):
            if i not in self.visited:
                self.temp = set()
                solution(i)
                self.answer = max(self.answer, len(self.temp))
        
        return self.answer
            
        
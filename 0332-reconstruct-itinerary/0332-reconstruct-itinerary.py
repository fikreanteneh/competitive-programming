class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        path = defaultdict(list)
        for departure, arrival in tickets:
            path[departure].append(arrival)
       
        for departure, arrival in path.items():
            arrival.sort(reverse = True)
        self.target = len(tickets) + 1
        self.answer = []
        self.visited = defaultdict(set)
        def dfs(city):
            self.answer.append(city)
            
            if len(self.answer) == self.target:
                return self.answer
            n = len(path[city])
            for i in range(n - 1, -1, -1):
                if i not in self.visited[city]:
                    self.visited[city].add(i)
                    travel = dfs(path[city][i])
                    if travel:
                        return travel
                    self.visited[city].discard(i)
            self.answer.pop()
        
        
        return dfs("JFK")
        
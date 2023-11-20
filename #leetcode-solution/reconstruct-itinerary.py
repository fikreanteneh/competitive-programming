class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        path = defaultdict(list)
        for departure, arrival in tickets:
            path[departure].append(arrival)
       
        for departure, arrival in path.items():
            arrival.sort(reverse = True)
        self.answer = []
        stack = ["JFK"]
        while stack:
            if path[stack[-1]]:
                stack.append( path[stack[-1]].pop())
            else:
                self.answer.append( stack.pop() )
        self.answer.reverse()    
        return self.answer
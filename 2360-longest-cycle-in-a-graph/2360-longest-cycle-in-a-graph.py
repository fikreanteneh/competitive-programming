class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.answer = -1
        path = set()
        
        def solution(node):
            if node < 0:
                return False
            if node in path:
                return [node, 1]
            
            temp = edges[node]
            edges[node] = -2
            path.add(node)
            
            nextt = solution(temp)
            path.discard(node)
            
            if nextt:
                if nextt[0] == node:
                    self.answer = max(self.answer, nextt[1])
                    return False
                nextt[1] += 1
                return nextt
            return False
        for i in range(len(edges)):
            solution(i)
            
        return self.answer
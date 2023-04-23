class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        visited = set()
        self.answer = -1
        path = set()
        
        def solution(node):
            if node in path:
                return [node, 1]
            if node in visited or node == -1:
                return False
            visited.add(node)
            path.add(node)
            # print( node, ">>", edges[node])
            nextt = solution(edges[node])
            
            # print(node, nextt, path)
            path.discard(node)
            if nextt:
                nextt[1] += 1
                if nextt[0] == node:
                    self.answer = max(self.answer, nextt[1] - 1)
                    # print(self.answer, nextt[1])
                    nextt = False
                return nextt
            return False
        # solution(0)   
        for i in range(len(edges)):
            solution(i)
            
        return self.answer
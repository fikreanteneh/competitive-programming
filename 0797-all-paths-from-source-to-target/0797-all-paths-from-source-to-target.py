class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        stack = [0]
        n  = len(graph) - 1
        
        
        def solution(root):
            if root == n:
                if len(stack) > 1:
                    answer.append(stack.copy())
                return
            for neighbor in graph[root]:
                stack.append(neighbor)
                solution(neighbor)
                stack.pop()
            
        solution(0)
        return answer
            
                
                
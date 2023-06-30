class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: set())
        for i, j in adjacentPairs:
            graph[i].add(j)
            graph[j].add(i)
        
        que = deque([])
        for i, j in graph.items():
            if len(j) == 1: 
                que.append(i)
                break
                
        answer = []
        while que:
            curr = que.pop()
            answer.append(curr)
            for child in graph[curr]:
                que.append(child)
                graph[child].discard(curr)
        
        return answer
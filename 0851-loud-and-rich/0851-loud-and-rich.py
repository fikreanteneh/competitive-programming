class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        n = len(quiet)
        
        graph = [[] for _ in range(n)]
        incoming = [0 for _ in range(n)]
        answer = [i for i in range(n)]
        
        
        for a, b in richer:
            graph[a].append(b)
            incoming[b] += 1
        
        que = deque([])
        for i, val in enumerate(incoming):
            if val == 0:
                que.append(i)
                
        while que:
            node = que.popleft()
            for child in graph[node]:
                if quiet[answer[node]] <= quiet[answer[child]]:
                    answer[child] = answer[node]
                incoming[child] -= 1
                if incoming[child] == 0:
                    que.append(child)
        
        return answer
            
        
        
        
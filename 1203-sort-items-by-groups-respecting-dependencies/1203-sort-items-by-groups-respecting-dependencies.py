class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groups = {}
        
        start = -1
        for i,val in enumerate(group):
            if val == -1:
                groups[start] = [i]
                group[i] = start
                start -= 1
            else:
                g = groups.setdefault(val, set())
                g.add(i)
        
        def topSort(graph):
            que = deque([])
            for i, j in graph.items():
                if j[1] == 0:
                    que.append(i)
            ordered = []
            while que:
                node = que.pop()
                ordered.append(node)
                for child in graph[node][0]:
                    graph[child][1] -= 1
                    if graph[child][1] == 0:
                        que.appendleft(child)
                graph.pop(node)
            if graph:
                return False
            return ordered
        
        groupGraph = {i: [set(), 0] for i in groups.keys() }
        
        for par, gr in groups.items():
            graph = {i: [set(), 0] for i in gr }
            for node in gr:
                before = beforeItems[node]
                for i, item in enumerate(before):
                    if item not in gr:
                        if not par in groupGraph[group[item]][0]:
                            groupGraph[group[item]][0].add(par)
                            groupGraph[par][1] += 1
                        continue
                    graph[item][0].add(node)
                    graph[node][1] += 1
            if par < 0:
                continue
            ordered = topSort(graph)
            if not ordered:
                return []
            groups[par] = ordered
        ordered = topSort(groupGraph)
        if not ordered:
            return []
        answer = []
        for order in ordered:
            answer.extend(groups[order])
        return answer
        
        
                
                
                
            
            
        
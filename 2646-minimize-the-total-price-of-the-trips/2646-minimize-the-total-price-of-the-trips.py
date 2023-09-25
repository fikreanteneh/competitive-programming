class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        repeated = defaultdict(int)
        neigh = [ [] for i in range(n)]
        for x, y in edges:
            neigh[x].append(y)
            neigh[y].append(x)
        edges = neigh
        def pathFind(node, target, visited):
            if node == target:
                return [node]
            
            for child in edges[node]:
                if child not in visited:
                    visited.add(child)
                    path = pathFind(child, target, visited)
                    if path:
                        path.append(node)
                        return path
            return []
        
        for start, dest in trips:    
            paths = pathFind(start, dest, {start})
            for path in paths:
                repeated[path] += 1
        def dfs(node, visited):
            store = []
            for child in edges[node]:
                if child not in visited:
                    visited.add(child)
                    store.append(dfs(child, visited))
            nodePrice = price[node]
            freq = repeated[node]
            answer = [nodePrice//2 * freq , nodePrice * freq]
            for colored, uncolored in store:
                answer[0] += uncolored
                answer[1] += min(colored, uncolored)
            return answer
        
        return min(dfs(0, {0}))
                
                    
            
            
        
        
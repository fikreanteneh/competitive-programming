class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [ [] for i in range(n) ]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        answer = [0] * n   
        visited= set()
        def solution(node):   
            if node in visited:
                return defaultdict()
            visited.add(node)
            # if isinstance(graph[node], defaultdict):
            #     return graph[node]
            store = defaultdict(int)
            store[labels[node]] += 1

            for child in graph[node]:
                mergeTwoDict(store, solution(child))
            # graph[node] = store
            answer[node] += store[labels[node]]
            return store
        
        def mergeTwoDict(dict1, dict2):
            for letter, num in dict2.items():
                dict1[letter] += num
        # for node in range(n):
        #     if isinstance(graph[node], list):
        #         solution(node)
        # for node in range(n):
        #     answer[node] = graph[node][labels[node]]
        # print(graph)
        solution(0)
        return answer
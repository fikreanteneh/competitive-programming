class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
        answer = set()
        totalCount = set()
        for i in range(n):
            if i in totalCount:
                continue
            curr = [i]
            answer.add(i)
            totalCount.add(i)
            while curr:
                j = curr.pop()
                for node in graph[j]:
                    if node in answer:
                        answer.discard(node)
                        continue
                    if node in totalCount:
                        continue
                    curr.append(node)
                    totalCount.add(node)
        return answer
            
            
        
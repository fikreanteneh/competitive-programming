class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.nodes = {i:set() for i in range(n)}
        
        for i in edges:
            self.nodes[i[0]].add(i[1])
            self.nodes[i[1]].add(i[0])
        ans = []
        visited = set()
        for k, v in self.nodes.items():
            if k in visited:
                continue
            main = set()
            stack = deque([k])
            while stack:
                # print (stack, k, v)
                x = stack.pop()
                if x in visited:
                    continue
                main.add(x)
                visited.add(x)
                for i in self.nodes[x]:
                    stack.appendleft(i)
            ans.append(main)
        curr = 0
        answer = 0
        # print(ans)
        for i, val in enumerate(ans):
            answer += (curr * len(val))
            curr += len(val)
        return answer
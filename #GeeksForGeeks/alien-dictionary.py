#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        if len(alien_dict) == 1:
            return list(set(list(alien_dict[0])))
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for i in range(1, N):
            left, right = alien_dict[i - 1], alien_dict[i]
            index = 0
            n, m = len(left), len(right)
            index = 0
            reach = min(n, m)
            def update(a):
                for i in a:
                    incoming[i] += 0
            update(left)
            update(right)
            for x, y in zip(left, right):
                if x != y:
                    graph[x].append(y)
                    incoming[y] += 1
                    break
                
                
        que = deque([])
        answer = []
        for i, val in incoming.items():
            if val == 0:
                que.append(i)

        while que:
            node = que.popleft()
            answer.append(node)
            for child in graph[node]:
                incoming[child] -= 1
                if incoming[child] == 0:
                    que.append(child)
        return answer

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		incoming = [len(i) for i in adj]
		que = deque([])
		answer = []
		for i, val in enumerate(incoming):
		    if val == 0:
		        answer.append(i)
		    elif val == 1:
		        que.append(i)
		    
		    while que:
		        node = que.popleft()
		        answer.append(node)
		        for child in adj[node]:
		            incoming[child] -= 1
		            if incoming[child] == 1:
		                que.append(child)
		if len(answer) == len(adj):
		    return 0
		return 1

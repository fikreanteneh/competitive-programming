"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        store = {}
        def solution(node):
            if node.val in store:
                return store[node.val]
            new = Node(node.val)
            store[node.val] = new
            for neighbor in node.neighbors:
                new.neighbors.append(solution(neighbor))
            return new
        return solution(node)
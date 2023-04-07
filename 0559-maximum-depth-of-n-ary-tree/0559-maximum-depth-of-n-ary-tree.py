"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
                return 0
        def solution(root, depth):
            
            maxi = depth
            if root.children:
                for i in root.children:
                    maxi = max(solution(i, depth + 1), maxi)
            return maxi
        return solution(root, 1)
            
            
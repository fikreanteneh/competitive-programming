"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def solution(root, answer):
            if not root:
                return
            answer.append(root.val)
            for i in root.children:
                solution(i, answer)
        answer = []
        solution(root, answer)
        return answer
        
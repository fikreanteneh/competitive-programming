# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.answer = 0
        parents = (1,1)
        def solution(node, parents):
            if not node:
                return
            increase = 0 if parents[0] % 2 else node.val
            self.answer += increase
            
            solution(node.left, (parents[-1], node.val))
            solution(node.right, (parents[-1], node.val))
        
        solution(root, parents)
        return self.answer
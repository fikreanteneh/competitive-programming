# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def move(root, value):
            if root.val == value.val:
                return -1
            elif root.val < value.val:
                return 1
            else:
                return 0
        pnext = move(root, p)
        qnext = move(root, q)
        if pnext != qnext or min(pnext, qnext) == -1:
            return  root
        nextt = [root.left, root.right]
        return self.lowestCommonAncestor(nextt[pnext], p, q)
        
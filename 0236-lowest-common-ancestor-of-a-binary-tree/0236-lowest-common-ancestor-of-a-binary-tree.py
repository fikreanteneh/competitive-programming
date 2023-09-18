# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def sol(root):
            if not root: return False
            
            curr = root == p or root == q
            left = sol(root.left)
            right = sol(root.right)
            values = left if left else right
            
            if type(values) == TreeNode:
                return values
            
            if (left and right) or (curr and (left or right)):
                return root
            
            return (left or right or curr)
        
        return sol(root)
            
        
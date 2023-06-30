# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        head = TreeNode(None)
        self.newH = head
        def sol(root):
            if not root:
                return
            sol(root.left)
            self.newH.right = TreeNode(root.val)
            self.newH = self.newH.right
            sol(root.right)
        sol(root)
        return head.right
            
            
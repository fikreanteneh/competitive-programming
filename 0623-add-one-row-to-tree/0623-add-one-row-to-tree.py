# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        newRoot = TreeNode(0, root)
        
        def dfs(root, dep):
            if not root:
                return
            if dep == depth:
                left = TreeNode(val, root.left, None)
                right = TreeNode(val, None, root.right)
                root.left = left
                root.right = right
                return
            dfs(root.left, dep + 1)
            dfs(root.right, dep + 1)
        
        dfs(newRoot, 1)
        return newRoot.left
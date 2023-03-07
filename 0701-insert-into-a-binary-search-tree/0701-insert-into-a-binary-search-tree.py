# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root, val):
            x, y = None, None
            if not root:
                return TreeNode(val)
            if val > root.val:
                x = insert(root.right, val)
            else:
                y = insert(root.left, val)
            if x:
                root.right = x
            elif y:
                root.left = y
            return None
        new = root
        z = insert(new, val)
        return root if root else z
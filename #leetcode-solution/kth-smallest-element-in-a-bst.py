# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.ans = -1
        def inorder(node, curr):
            if not node:
                return 0 + curr
            curr = inorder(node.left, curr) + 1
            if curr == k:
                self.ans = node.val
            return inorder(node.right, curr)
        inorder(root, 0)
        return self.ans
            
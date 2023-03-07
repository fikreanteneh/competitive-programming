# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode], depth = 0) -> int:
        if not root:
            return depth
        
        depth += 1
        
        left = self.minDepth(root.left, depth)
        right = self.minDepth(root.right, depth)
        
        if left == depth or right == depth:
            return max(left, right)
        return min(left, right)
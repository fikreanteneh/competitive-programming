# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solution(p, q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if not q and p:
                return False
            if p.val != q.val:
                return False
            left = solution(p.left, q.right)
            right = solution(p.right, q.left)
            return left and right
        if not root:
            return True
        return solution(root.left, root.right)
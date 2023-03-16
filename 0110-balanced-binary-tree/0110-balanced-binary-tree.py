# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def solution(root):
            if not root:
                return 0
            left = solution(root.left)
            right = solution(root.right)
            if type(left) != int or type(right) != int:
                return False
            if abs(left-right) > 1:
                return False
            return max(right, left) + 1
        
        
        return bool(solution(root))

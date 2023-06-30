# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float("-inf")
        
        def solution(root):
            if not root:
                return 0
            left = solution(root.left) + root.val
            right = solution(root.right) + root.val
            self.maxi = max(self.maxi, left + right - root.val, root.val, left, right)
            return max(left, right, root.val)
        solution(root)
        return self.maxi
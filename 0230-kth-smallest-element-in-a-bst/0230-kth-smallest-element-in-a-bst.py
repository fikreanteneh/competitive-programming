# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.answer = float("-inf")
        def solution(root):
            if not root:
                return float
            
            solution(root.left)
            self.k -= 1
            if not self.k:
                self.answer = root.val
            solution(root.right)
            
        solution(root)
        return self.answer
        
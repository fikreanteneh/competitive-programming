# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if (left == 1 or right == 1):
                self.ans += 1
                return 2
            if (left == 2 or right == 2):
                return 0
            return 1

        answer = dfs(root)
        if answer == 1:
            self.ans += 1
        return self.ans
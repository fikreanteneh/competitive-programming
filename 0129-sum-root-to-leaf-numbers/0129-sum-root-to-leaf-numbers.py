# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        self.total = 0
        
        def solution(root):
            if not root:
                return
            stack.append(str(root.val))
            if not root.left and not root.right:
                add = int( "".join(stack))
                self.total += add
                stack.pop()
                return
            solution(root.left)
            solution(root.right)
            stack.pop()
                
        solution(root)
        return self.total
        
        
        
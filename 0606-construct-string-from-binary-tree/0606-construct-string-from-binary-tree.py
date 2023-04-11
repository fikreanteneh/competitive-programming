# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        stack = []
        def solution(root):
            if not root:
                return
            stack.append(str(root.val))
            nodes = (root.left, root.right)
            for node in nodes:
                stack.append("(")
                solution(node)
                stack.append(")")
            if stack[-2] == "(":
                if stack[-4] == "(":
                    for i in range(-1,-5, -1):
                        stack[i] = ""
                else:
                    stack[-1], stack[-2] = "", ""
        
        solution(root)
        return "".join(stack)
        

            
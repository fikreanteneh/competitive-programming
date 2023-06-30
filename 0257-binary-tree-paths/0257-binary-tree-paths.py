# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = []
        answer = []
        def solution(root):
            if not root:
                return
            
            stack.append(str(root.val))
            stack.append("->")
        
            if not root.left and not root.right:
                stack.pop()
                answer.append("".join(stack))
                stack.pop()
                return
            
            solution(root.left)
            solution(root.right)
            stack.pop()
            stack.pop()
        
                         
        solution(root)
        return answer
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def solution(root, answer):
            if not root:
                return
            solution(root.left, answer)
            solution(root.right, answer)
            answer.append(root.val)
            
        answer = []
        solution(root, answer)
        return answer
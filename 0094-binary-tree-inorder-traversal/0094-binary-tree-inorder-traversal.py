# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def solution(root, answer):
            if not root:
                return
            solution(root.left, answer)
            answer.append(root.val)
            solution(root.right, answer)
            return
        answer = []
        solution(root, answer)
        return answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def solution(node):
            if not node:
                return [0, 0]
            prev1, nextPrev1 = solution(node.left)
            prev2, nextPrev2 = solution(node.right)
            return [node.val + nextPrev1 + nextPrev2, 
                    max(prev1 + prev2, nextPrev1 + nextPrev2, prev1 + nextPrev2, prev2 + nextPrev1)]
        root = TreeNode(0, root)
        return max(solution(root))
            
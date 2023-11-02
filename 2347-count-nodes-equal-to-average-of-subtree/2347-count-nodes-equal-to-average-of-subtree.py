# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def solution(root, answer):
            if not root:
                return (0, 0)
            left = solution(root.left, answer)
            right = solution(root.right, answer)
            sums = left[0] + right[0] + root.val
            total = left[1] + right[1] + 1
            if root.val == ( sums // total):
                answer[0] += 1
            return (sums, total)
        
        answer = [0]
        solution(root, answer)
        return answer[0]
        
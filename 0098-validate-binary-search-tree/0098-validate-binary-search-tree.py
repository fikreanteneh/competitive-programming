# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solution(root, compare):
            if not root:
                return True
            
            if root.val <= compare[0] or root.val >= compare[1]:
                return False
            
            compare1 =  (compare[0], root.val)
            compare2 = (root.val, compare[1])

            return solution(root.left, compare1) and solution(root.right, compare2)
        

        return solution(root.left, (float("-inf"), root.val)) and solution(root.right, (root.val,  float("inf")))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        answer = []
        arr = []
        def sol(node, sums):
            if not node:
                return
            sums += node.val
            arr.append(node.val)
            if not node.left and not node.right:
                if sums == targetSum:
                    answer.append(arr.copy())
                arr.pop()
                return
            sol(node.left, sums)
            sol(node.right, sums)
            arr.pop()
        
        sol(root, 0)
        return answer
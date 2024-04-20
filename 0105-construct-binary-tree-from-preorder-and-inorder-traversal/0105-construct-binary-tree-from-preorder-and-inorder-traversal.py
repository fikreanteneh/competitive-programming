# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        n = len(preorder)
        preorder.extend([float("inf"), float("inf")])
        
        def solve(left, mid ,right):
            node = TreeNode(inorder[mid])
            if self.index >= n:
                return None
            for i in range(left, mid):
                if preorder[self.index + 1] == inorder[i]:
                    self.index += 1
                    node.left = solve(left, i, mid - 1)
            for i in range(mid + 1, right + 1):
                if preorder[self.index + 1] == inorder[i]:
                    self.index += 1
                    node.right = solve(mid + 1, i, right)
            return node
        
        return solve(0, inorder.index(preorder[0]), n - 1)
                
            
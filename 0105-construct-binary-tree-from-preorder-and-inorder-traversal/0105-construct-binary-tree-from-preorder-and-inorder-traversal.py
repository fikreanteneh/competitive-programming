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
        preorder.extend([float("-inf"), float("inf")])
        inorder.extend([float("-inf"), float("inf")])
        
        mapp = {}
        for i, element in enumerate(inorder):
            mapp[element] = i
            
        def solve(left, mid ,right):
            if self.index >= n:
                return None
            
            node = TreeNode(inorder[mid])
            
            if left <= mapp[preorder[self.index + 1]] < mid:
                self.index += 1
                node.left = solve(left, mapp[preorder[self.index ]], mid - 1)
                
            if mid < mapp[preorder[self.index + 1]] <= right:
                self.index += 1
                node.right = solve(mid + 1, mapp[preorder[self.index]], right)
            return node
        
        return solve(0, inorder.index(preorder[0]), n - 1)
                
            
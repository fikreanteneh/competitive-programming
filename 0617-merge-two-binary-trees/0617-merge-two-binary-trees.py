# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def createNew(root1, root2, prev, pos):
            if not root1 and not root2: 
                return
            new = TreeNode( (0 if not root1 else root1.val) + (0 if not root2 else root2.val))
            if pos == "left":
                prev.left = new
            else:
                prev.right = new
                
            r1 = root1.left if root1 else root1
            r2 = root2.left if root2 else root2
            r3 = root1.right if root1 else root1
            r4 = root2.right if root2 else root2
            createNew(r1, r2, new, "left")
            createNew(r3, r4, new, "right")
        
        mergedNode = TreeNode(float("inf"))
        createNew(root1, root2, mergedNode, "left")
        return mergedNode.left
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode(float("inf"), root)
        def getReplacingNode(node):
            child = node.right
            while child.right:
                node, child = child, child.right
            node.right = child.left
            child.left = None
            return child
            
        def solve(node):
            if not node:
                return None
            elif node.val == key:
                if not node.left:
                    return node.right
                if not node.left.right:
                    node.left.right = node.right
                    return node.left
                replacingNode = getReplacingNode(node.left)
                replacingNode.left = node.left
                replacingNode.right = node.right
                return replacingNode
                    
            elif node.val > key:
                node.left = solve(node.left)
                return node
            else:
                node.right = solve(node.right)
                return node
        
        solve(dummy)
        return dummy.left
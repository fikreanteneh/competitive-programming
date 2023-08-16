# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        
        def helper(index, depth):
            if index >= n:
                return (0, index)
            index2 = index 
            while traversal[index2] == "-":
                index2 += 1
                
            if index2 - index != depth:
                return (0,index)
            index3 = index2
            
            while index3 < n and traversal[index3].isnumeric():
                index3 += 1
            return (int(traversal[index2:index3]), index3)
        
        def sol(node, depth, index):
            
            if index >= n:
                return n
            
            leftVal, pos = helper(index, depth) 
            if not leftVal:
                return pos
            node.left = TreeNode(leftVal)
            index = sol(node.left, depth + 1, pos)
            
            rightVal, pos = helper(index, depth) 
            if not rightVal:
                return pos
            node.right = TreeNode(rightVal)
            index = sol(node.right, depth + 1, pos)
            
            return index
        val, index = helper(0,0)
        root = TreeNode(val)   
        sol(root, 1, index)
        return root
            
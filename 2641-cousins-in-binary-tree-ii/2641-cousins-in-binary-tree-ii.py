# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        levelSum = root.val
        level = deque([root])
        
        
        while level:
            newSum = 0
            length = len(level)
            for i in range(length):
                
                node = level.pop()
                node.val = levelSum - node.val
                
                left = node.left.val if node.left else 0
                right = node.right.val if node.right else 0
                sibiling = left + right
                newSum += sibiling
                if node.left:
                    node.left.val = sibiling
                    level.appendleft(node.left)
                if node.right:
                    node.right.val = sibiling
                    level.appendleft(node.right)
            levelSum = newSum
        
        return root
                

                
                
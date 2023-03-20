# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        mode = []
        self.current = float("inf")
        self.count = 0
        
        def solution(root):
            if not root:
                return
            solution(root.left)
            
            if self.current == root.val:
                self.count += 1
            else:
                self.current = root.val
                self.count = 1
                
            while mode and mode[-1][-1] < self.count:
                mode.pop()
            if not mode or self.count >= mode[-1][-1]:
                mode.append((self.current, self.count))
                
            solution(root.right)
        solution(root)
        for i, val in enumerate(mode):
            mode[i] = val[0]
        return mode
            
        
        
                
            
        
        
        
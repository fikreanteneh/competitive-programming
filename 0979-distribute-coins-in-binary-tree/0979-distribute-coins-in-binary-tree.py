# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return(0,0)
            
            x, y = dfs(node.left)
            a, b = dfs(node.right)
            new = [x + a, y + b]
            self.ans += sum(new)
            if node.val == 0:
                new[1] += 1
            else:
                new[0] += (node.val - 1)
            
            extra = max(0, new[0] - new[1] )
            need  =  max(0, new[1] - new[0])
            
            # print(node.val)
            # print((x,y))
            # print((a,b))
            # print(new)
#             print((extra, need))
#             print()
            
            
            return (extra, need)
        
        dfs(root)
        return self.ans
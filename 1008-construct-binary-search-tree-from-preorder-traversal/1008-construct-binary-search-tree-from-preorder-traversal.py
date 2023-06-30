# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        stack = [TreeNode(preorder[0])]
        stack2 = [(float("-inf"), preorder[0] , float("inf"))]
        
        for i in range(1,len(preorder)):
            val = preorder[i]
            while not (stack2[-1][0] < val < stack2[-1][1] ) and not (stack2[-1][1] < val < stack2[-1][2]):
                stack.pop()
                stack2.pop()
                
            temp = TreeNode(val)
            
            if stack[-1].val > val:
                stack[-1].left = temp  
                stack2.append((stack2[-1][0], val, stack2[-1][1]))
            else:
                stack[-1].right = temp
                stack2.append((stack2[-1][1] ,val, stack2[-1][2]))

            stack.append(temp)
        return stack[0]
            
        
        
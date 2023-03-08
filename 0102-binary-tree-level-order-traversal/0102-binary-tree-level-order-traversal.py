# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solution(roots, answer):
            temp = []
            newRoots = []
            for root in roots:
                temp.append(root.val)
                if root.left:
                    newRoots.append(root.left)
                if root.right:
                    newRoots.append(root.right)
            answer.append(temp)
            if newRoots:
                solution(newRoots, answer)
            
        answer = []
        if root:
            solution([root], answer)
        return answer
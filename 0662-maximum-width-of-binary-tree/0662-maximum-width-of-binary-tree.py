# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        breadth = deque([(root, 1)])
        answer = 0
        while breadth:
            answer = max(answer, breadth[0][1] - breadth[-1][1])
            n = len(breadth)
            for i in range(n):
                temp = breadth.pop()
                if temp[0].left:
                    breadth.appendleft((temp[0].left, (temp[1] * 2) - 1))
                if temp[0].right:
                    breadth.appendleft((temp[0].right, temp[1] * 2))
        return answer + 1
                    
            
        
        
#         track = [0, 0]
        
#         def solution(root, pos):
#             if not root:
#                 return
            
#             track[0] = min(track[0], pos)
#             track[1] = max(track[0], pos)
            
#             solution(root.left, pos - 1)
#             solution(root.right, pos + 1)
        
#         solution(root, 0)
#         return track[1] - track[0]
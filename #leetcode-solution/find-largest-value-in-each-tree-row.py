# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        answer = []
        que = deque([root])
        
        while que:
            length = len(que)
            rowAns = float("-inf")
            for _ in range(length):
                node = que.pop()
                rowAns = max(rowAns, node.val)
                if node.left: 
                    que.appendleft( node.left)
                if node.right: 
                    que.appendleft( node.right)
            answer.append(rowAns)
        return answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return []
        que = deque([root])
        while que:
            temp = []
            length = len(que)
            for _ in range(length):
                node = que.pop()
                temp.append(node.val)
                if node.left:
                    que.appendleft(node.left)
                if node.right:
                    que.appendleft(node.right)
            answer.append(temp)
        answer.reverse()
        return answer
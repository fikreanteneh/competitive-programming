# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete.append(0)
        to_delete = set(to_delete)
        answer = []
        def dfs(node, parent):
            if not node:
                return 
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            if left:
                node.left = None
            if right:
                node.right = None
            if node.val not in to_delete and parent in to_delete:
                answer.append(node)
            return node.val in to_delete
        dfs(root, 0)
        return answer
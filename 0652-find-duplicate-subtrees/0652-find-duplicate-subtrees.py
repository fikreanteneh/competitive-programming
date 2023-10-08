# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        @cache
        def compare(node1, node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (node2 and not node1) or (node1.val != node2.val):
                return False
            return compare(node1.left, node2.left) and compare(node1.right, node2.right)
        answer = set()     
        store = defaultdict(list)
        def dfs(node):
            if not node:
                return
            flag = False
            for neigh in store[node.val]:
                if compare(node, neigh):
                    answer.add(neigh)
                    flag = False
                    break
            if not flag:
                store[node.val].append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return list(answer)
                    
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list)
        
        def solution(root, pos, row):
            if not root:
                return
            store[pos].append((row,root.val))
            solution(root.left, pos - 1, row + 1)
            solution(root.right, pos + 1, row + 1)
        
        solution(root, 0, 0)
        answer = []
        for i,j in store.items():
            j.sort()
        store = list(store.items())
        store.sort()
        for i, values in enumerate(store):
            for k, val in enumerate(values[1]):
                values[1][k] = val[1]
            store[i] = values[1] 
        return store
        
            
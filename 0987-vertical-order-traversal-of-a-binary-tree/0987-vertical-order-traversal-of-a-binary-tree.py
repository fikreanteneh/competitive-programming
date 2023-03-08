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
        i = -1
        while i in store:
            temp = []
            for j in store[i]:
                temp.append(j[1])
            answer.append(temp)
            i -= 1
        answer.reverse()
        i = 0
        while i in store:
            temp = []
            for j in store[i]:
                temp.append(j[1])
            answer.append(temp)
            i += 1
        return answer
        
            
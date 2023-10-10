# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        store = defaultdict(int)
        store[0] = 1
        self.answer= 0
        def solution(root, sums):
            if not root:
                return
            sums += root.val
            check = sums - targetSum
            self.answer += store[check]
            store[sums] += 1
            solution(root.left, sums)
            solution(root.right, sums)
            store[sums] -= 1
        solution(root, 0)
        return self.answer
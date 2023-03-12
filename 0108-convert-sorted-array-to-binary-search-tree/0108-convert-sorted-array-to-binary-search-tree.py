# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        leftt, rightt = 0, len(nums) - 1
        
        def solution(leftPointer, rightPointer):
            if leftPointer > rightPointer:
                return None
            mid = leftPointer + ((rightPointer - leftPointer) // 2)
            node = TreeNode(nums[mid])
            node.left = solution(leftPointer, mid - 1)
            node.right = solution(mid + 1, rightPointer)
            return node
        
        return solution(leftt, rightt)
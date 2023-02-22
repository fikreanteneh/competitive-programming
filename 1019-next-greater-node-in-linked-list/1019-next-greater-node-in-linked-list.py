# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        new = head
        while head:
            while stack and stack[-1].val < head.val:
                stack.pop().val = head.val
            stack.append(head)
            head = head.next
        while stack:
            stack.pop().val = 0
        while new:
            ans.append(new.val)
            new = new.next
            
        
        
        return  ans
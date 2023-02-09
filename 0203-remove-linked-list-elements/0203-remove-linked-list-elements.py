# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head = ListNode(None, head)
        left, right = head, head.next
        while right:
            if val == right.val:
                left.next = right.next
                right = right.next
            else:
                left, right = left.next, right.next
        
        return head.next
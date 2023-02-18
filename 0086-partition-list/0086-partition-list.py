# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(None, None)
        right = ListNode(None, None)
        new, l, r = head, left, right
        while head:
            if head.val < x:
                l.next = ListNode(head.val)
                l = l.next
            else:
                r.next = ListNode(head.val)
                r = r.next
            head = head.next
        l.next = right.next
        return left.next
            
        
#         if head.next is None:
#             return head
#         head = ListNode(float("-inf"), head)
#         front, back = head , head
#         while front and back:
#             while front.next and front.next.val < x:
#                 front = front.next
#             new = front
#             while new.next and new.next.val >= x:
#                 new = new.next
#             temp = new.next
#             front.next, new.next = new.next, front.next
            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        new = None
        old = head
        while old:
            count += 1
            if old.next is None and count == n-1: 
                head = head.next
                break
            elif count == n: new = head

            old = old.next
            if old is None :
                new.next = new.next.next
                break
            elif count > n: new = new.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        head = ListNode("dummy", head)
        new, old = head, head.next 
        while old:
            count += 1
            old = old.next
            if old is None :
                new.next = new.next.next
                break
            if count >= n: new = new.next
        return head.next

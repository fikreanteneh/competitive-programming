# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast = slow = head
        bo = True
        while fast and fast.next and bo:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                bo = False

        if fast != slow:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        head = ListNode(None, head)
        head = ListNode(None, head)
        fast, slow = head.next.next, head
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
        return fast == slow
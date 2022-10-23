# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = back = head
        c = 1
        for i in range(k - 1):
            front = front.next
        change = front
        while front.next:
            front, back = front.next, back.next
        change.val, back.val = back.val, change.val
        return head

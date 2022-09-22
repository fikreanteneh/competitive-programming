# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        y = head
        count = 0
        while x.next is not None and y.next is not None:
            x = x.next
            if count%2 == 0: y = y.next
            count += 1
        return y

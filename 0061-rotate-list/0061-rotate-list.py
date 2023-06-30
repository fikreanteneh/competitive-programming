# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front = None
        back = head
        count = 0
        if head is None or head.next is None: return head
        while back: 
            back = back.next
            count += 1
        k, count, back = k%count, 0, head
        if k == 0: return head
        while back.next:
            back = back.next
            count+= 1
            if back.next is None and count < k: 
                back = head
                count += 1
            
            if k == count: front = head
            elif front: front = front.next
        back.next = head
        main = front.next
        front.next = None
        return main
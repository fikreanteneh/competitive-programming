# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        head = ListNode("None", head)
        h1, h2 = head, head.next
        back = head
        front = head.next
        while front and front.next:
            back.next = front.next
            front.next = front.next.next
            back = back.next
            if front.next:
                front = front.next
        back.next = None
        front.next = h1.next
        
        
        
        
        return h2
        
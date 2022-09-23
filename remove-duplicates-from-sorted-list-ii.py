# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back = ListNode(-200, head)
        head = back
        front = head.next
        while front:
            if front.next and front.val == front.next.val:
                while front.next and front.val == front.next.val:
                    front = front.next
                back.next = front.next
            else:
                back = back.next
            front = front.next      
        return head.next

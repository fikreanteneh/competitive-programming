# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None, head)
        back, front = head, head.next
        
        while front:
            while front and front.val == back.val:
                front = front.next
            back.next = front
            back = front
            if front:
                front = front.next
        
        
        return head.next
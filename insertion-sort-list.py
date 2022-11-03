# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = head
        head = ListNode(float("-inf"))
        while front:
            back = head
            new = head.next
            while new and new.val <= front.val:
                back = back.next
                new = new.next
            back.next = ListNode(front.val, new)
            front = front.next
        return head.next
                

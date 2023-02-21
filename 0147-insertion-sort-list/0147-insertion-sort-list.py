# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(float("-inf"), head)
        back, front = head, head.next
        while front:
            left, right = head, head.next
            while right.val < front.val and right != front:
                right = right.next
                left = left.next
            if right != front:
                t2 = front.next
                front.next = right
                left.next = front
                back.next = t2
                front = t2
                new = head
                continue
            back = back.next
            front = front.next
            
        return head.next
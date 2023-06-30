# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        head = ListNode(None, head)
        cur = head
        while cur.next:
            back = cur.next
            front = cur.next
            i = k
            while front and i > 1:
                front = front.next
                i -= 1
            if front is None:
                break
            prev, prev1 = back, back.next
            for i in range(1, k):
                temp, temp1 = prev1, prev1.next
                prev1.next = prev
                prev1 = temp1
                prev = temp
            cur.next, back.next = prev, prev1
            cur = back
        return head.next
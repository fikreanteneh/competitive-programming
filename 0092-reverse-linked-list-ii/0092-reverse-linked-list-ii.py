# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        head = ListNode("dummy", head)
        point = head
        leftN = head.next
        count = 1
        while count < left:
            point = point.next
            leftN = leftN.next
            count += 1
        leftMost = leftN
        rightN = leftN.next if leftN else None
        while count < right - 1:
            temp = rightN.next
            rightN.next = leftN
            leftN = rightN
            rightN = temp
            count += 1
        if leftMost and rightN:
            leftMost.next = rightN.next
            rightN.next = leftN
            point.next = rightN
        return head.next
        
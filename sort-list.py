# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        new = head
        while new:
            nums.append(new.val)
            new = new.next
        nums.sort()
        head = ListNode()
        new = head
        for i in nums:
            x = ListNode(i)
            new.next = x
            new = new.next
        return head.next

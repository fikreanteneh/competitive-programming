# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = head
        while new and new.next:
            temp = new.next
            while temp and temp.val == new.val:
                temp = temp.next
            new.next = temp
            new = new.next
        return head

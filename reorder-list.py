# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        main = head
        stack = []
        while main:
            stack.append(main)
            main = main.next
        main = head
        for i in range(ceil(len(stack)//2)):
            temp = main
            main = main.next
            temp.next = stack.pop()
            temp.next.next = main
        main.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        head,carry = None, 0
        print(stack1, stack2)
        while stack1 or stack2:
            if len(stack1) == 0: stack1.append(0)
            elif len(stack2) == 0: stack2.append(0)
            value = stack1.pop() + stack2.pop() + carry
            if value > 9:
                carry = int(str(value)[0])
                value = int(str(value)[1])
            else: carry = 0
            head = ListNode(value, head)
        if carry > 0: head = ListNode(carry, head)
        return head

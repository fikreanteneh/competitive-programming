# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(node):
            count = 0
            prev = None
            curr = node
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count += 1
            return (count, prev)
        c1, l1  = reverseList(l1)
        c2, l2  = reverseList(l2)
        upper, lower = (l1, l2) if c1 >= c2 else (l2, l1)
        upper = ListNode(0, upper)
        lower = ListNode(0, lower)
        carry = 0
        up = upper
        while upper.next:
            sums = carry + upper.next.val
            if lower.next:
                sums += lower.next.val
                lower = lower.next
            upper.next.val, carry = sums%10, sums//10
            upper = upper.next
        if carry:
            upper.next = ListNode(carry)
        
        return reverseList(up.next)[1]
        
                
                
            
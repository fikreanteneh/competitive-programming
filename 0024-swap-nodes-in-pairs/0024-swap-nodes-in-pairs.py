# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeL = head
        head = ListNode("dummy", head)
        point = head
        if nodeL and nodeL.next:
            nodeR = nodeL.next
            while True :
                temp1 = nodeR.next
                point.next = nodeR
                nodeL.next = temp1
                nodeR.next = nodeL
                point, nodeL = nodeL, temp1
                if temp1 is None or temp1.next is None:
                    break
                nodeR = temp1.next
        return head.next
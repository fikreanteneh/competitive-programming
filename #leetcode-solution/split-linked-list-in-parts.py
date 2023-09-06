# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        answer = [ListNode(0) for _ in range(k)]
        new = head
        count = 0
        while new:
            count += 1
            new = new.next
        x = count//k
        y = count % k
        for i in range(k):
            answer[i].val += x
            if i < y: answer[i].val += 1
        for i, node in enumerate(answer):
            node.next = head
            for _ in range(node.val - 1):
                head = head.next
            if not head:
                break
            newHead = head.next
            head.next = None
            head = newHead
        return [node.next for node in answer]
            
        
        
            
        
        
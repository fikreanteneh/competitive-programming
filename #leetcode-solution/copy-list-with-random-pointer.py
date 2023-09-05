"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new = Node(head.val)
        
        newHead = new
        oldHead = head.next
        store = {head: new, None: None}
        
        while oldHead:
            node = Node(oldHead.val)
            store[oldHead] = node
            newHead.next = node
            newHead = newHead.next
            oldHead = oldHead.next
        
        oldHead = head
        newHead = new
        while newHead:
            newHead.random = store[oldHead.random]
            newHead = newHead.next
            oldHead = oldHead.next
        
        return new
            
            
            
            
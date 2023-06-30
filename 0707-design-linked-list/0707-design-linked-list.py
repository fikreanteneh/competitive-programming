class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1, self.head, None)
        self.head.next = self.tail
    def get(self, index: int) -> int:
        new = self.head.next
        while new.next and index > 0:
            new = new.next
            index -= 1
        return new.val
    def addAtHead(self, val: int) -> None:
        temp = Node(val, self.head, self.head.next)
        self.head.next.prev = temp
        self.head.next = temp
    def addAtTail(self, val: int) -> None:
        temp = Node(val, self.tail.prev, self.tail)
        self.tail.prev.next = temp
        self.tail.prev = temp
    def addAtIndex(self, index: int, val: int) -> None:
        new = self.head.next
        while new.next and index > 0:
            new = new.next
            index -= 1
        if index == 0:
            temp = Node(val, new.prev, new)
            new.prev.next = temp
            new.prev = temp
    def deleteAtIndex(self, index: int) -> None:
        new = self.head.next
        while new.next and index > 0:
            new = new.next
            index -= 1
        if new.next:
            new.prev.next, new.next.prev = new.next, new.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
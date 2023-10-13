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
    def printNodes(self):
        node = self.head
        while node:
            print(node.val, end= " >> ")
            node = node.next
        print()
    def addAtTail(self, val: int) -> None:
        temp = Node(val, self.tail.prev, self.tail)
        self.tail.prev.next = temp
        self.tail.prev = temp
    def deleteAtHead(self) -> None:
        new = self.head.next
        new.prev.next, new.next.prev = new.next, new.prev
        return new
    def deleteAtNode(self, new):
        new.prev.next, new.next.prev = new.next, new.prev

class LRUCache:

    def __init__(self, capacity: int):
        self.keys = [-1]*(10**4 + 1)
        self.keyNode = [None] * (10**4 + 1)
        self.cache = MyLinkedList()
        self.length = 0
        self.capacity = capacity
    

    def get(self, key: int) -> int:
        if self.keys[key] == -1:
            return -1
        node = self.keyNode[key]
        if node:
            self.cache.deleteAtNode(node)
            self.length -= 1
        self.cache.addAtTail(key)
        self.keyNode[key] = self.cache.tail.prev
        self.length += 1
        return self.keys[key]           

    def put(self, key: int, value: int) -> None:
        
        if self.keys[key] == -1:
            if self.length == self.capacity:
                node = self.cache.deleteAtHead()
                self.keys[node.val] = -1
                self.keyNode[node.val] = None
                self.length -= 1
            self.keys[key] = value
            self.cache.addAtTail(key)
            self.keyNode[key] = self.cache.tail.prev
            self.length += 1
        else:
            if self.keyNode[key]:
                self.cache.deleteAtNode(self.keyNode[key])
                self.cache.addAtTail(key)
                self.keys[key] = value
                self.keyNode[key] = self.cache.tail.prev
            elif self.length < self.capacity :
                self.cache.addAtTail(key)
                self.keys[key] = value
                self.keyNode[key] = self.cache.tail.prev
                self.length += 1
            else:
                node = self.cache.deleteAtHead()
                self.keys[node.val] = -1
                self.keyNode[node.val] = None
                self.cache.addAtTail(key)
                self.keys[key] = value
                self.keyNode[key] = self.cache.tail.prev
                
            
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
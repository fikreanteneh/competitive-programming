class Node:
    def __init__(self, key, val ,prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1,self.head, None)
        self.head.next = self.tail
        
    def get(self, key) -> int:
        new = self.head.next
        while new.next and new.key != key:
            new = new.next
        return new if new.key == key else self.tail
    
    def add(self, key, val) -> None:
        node = self.get(key)
        if node.key == key:
            node.val = val
            return
        temp = Node(key, val, node.prev, node)
        node.prev.next = temp
        node.prev = temp
    
    def delete(self, key) -> None:
        new = self.head.next
        while new.next and new.key != key:
            new = new.next
        if new and new.key == key:
            nnn, ppp = new.next, new.prev
            nnn.prev, ppp.next = ppp, nnn

class MyHashMap:

    def __init__(self, size = 10**4):
        self.size = (size + 10)
        self.keys = [MyLinkedList() for _ in range(self.size)]
    
    def hashFunction(self, value):
        hashedValue = hash(value)
        hashWithinRange = (hashedValue% (self.size - 10) )
        return hashWithinRange

    def put(self, key: int, value: int) -> None:
        index = self.hashFunction(key)
        self.keys[index].add(key, value)
        
    def get(self, key: int) -> int:
        index = self.hashFunction(key)
        return self.keys[index].get(key).val
        
    def remove(self, key: int) -> None:
        index = self.hashFunction(key)
        self.keys[index].delete(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
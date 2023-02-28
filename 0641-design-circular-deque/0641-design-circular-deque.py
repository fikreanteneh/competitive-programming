class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [-1]*k
        self.size = 0
        self.k = k
        self.front = 0
        self.back = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.front%self.k] = value
        self.front += 1
        self.size += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.back -= 1
        self.queue[self.back % self.k] = value
        self.size += 1
        return True
    

    def deleteFront(self) -> bool:
        if self.isEmpty(): 
            return False
        self.front -= 1
        self.size -= 1
        self.queue[self.front%self.k] = -1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.back] = -1
        self.size -= 1
        self.back += 1
        return True

    def getFront(self) -> int:
        return self.queue[(self.front-1)%self.k]

    def getRear(self) -> int:
        return self.queue[self.back%self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
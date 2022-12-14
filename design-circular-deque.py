class MyCircularDeque:
    
    def __init__(self, k: int):
        self.que = [None]*k
        self.size = k
        self.front = 0
        self.back = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        if self.back == self.front and self.que[self.front] is None: 
            self.que[self.front] = value
            return True
        self.front = (self.front + 1 )%self.size
        self.que[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        if self.back == self.front and self.que[self.front] is None: 
            self.que[self.front] = value
            return True
        self.back = self.back - 1
        if self.back < 0: self.back = self.size -1
        self.que[self.back] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        if self.front == self.back:
            self.que[self.front]=None
            return True
        self.que[self.front] = None
        self.front -= 1
        if self.front<0:self.front = self.size-1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        if self.front == self.back:
            self.que[self.front]=None
            return True
        self.que[self.back] = None
        self.back = (self.back+1)%self.size
        return True

    def getFront(self) -> int:
        if self.isEmpty():return -1
        return self.que[self.front]

    def getRear(self) -> int:
        if self.isEmpty():return -1
        return self.que[self.back]

    def isEmpty(self) -> bool:
        if self.front == self.back and self.que[self.front] is None:
            return True
        return False

    def isFull(self) -> bool:
        new = self.back
        new -= 1
        if new<0: new=self.size-1
        return new == self.front


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

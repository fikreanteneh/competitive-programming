class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.front = 0
        self.back = 0
        self.size = 0
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.queue[self.front] = value
        self.front += 1
        self.front %= self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if not self.size:
            return False
        self.queue[self.back] = -1
        self.size -= 1
        self.back += 1
        self.back %= self.k
        return True

    def Front(self) -> int:
        # if not self.size:
        #     return -1
        return self.queue[self.back]

    def Rear(self) -> int:
        # if not self.size:
        #     return -1
        return self.queue[self.front-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
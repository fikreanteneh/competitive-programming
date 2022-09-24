class MyQueue:
    def __init__(self):
        self.q = [None]
        self.first = 0
    def push(self, x: int) -> None:
        self.q.append(x)
    def pop(self) -> int:
        self.first+=1
        key = self.q[self.first]
        self.q[self.first] = None
        return key
    def peek(self) -> int:
        return self.q[self.first + 1]
    def empty(self) -> bool:
        if self.first == len(self.q)-1: return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

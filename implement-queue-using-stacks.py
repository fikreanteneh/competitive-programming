class MyQueue:
    def __init__(self):
        self.q = [None]
        self.first = 0
    def push(self, x: int) -> None:
        self.q.insert(1,x)
        self.first+=1
    def pop(self) -> int:
        key = self.q[self.first]
        if self.first > 0 :self.first -= 1
        return key
    def peek(self) -> int:
        return self.q[self.first]
    def empty(self) -> bool:
        if self.q[self.first] is None: return True
        return False

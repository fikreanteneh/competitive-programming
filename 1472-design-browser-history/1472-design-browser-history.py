class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.node = Node(homepage)
        self.curr = self.node

    def visit(self, url: str) -> None:
        new = Node(url, None, self.curr)
        self.curr.next = new
        self.curr = new

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev == None:
                break
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next == None:
                break
            self.curr = self.curr.next
        return self.curr.val      


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
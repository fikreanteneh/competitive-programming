class StockSpanner:

    def __init__(self):
        self.stack = [(float("inf"), 1)]

    def next(self, price: int) -> int:
        count = 1
        while price >= self.stack[-1][0]:
            count += self.stack.pop()[1]
        self.stack.append((price, count))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
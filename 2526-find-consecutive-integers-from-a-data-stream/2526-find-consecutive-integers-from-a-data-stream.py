class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.value = value
        self.k = k
        self.index = 0
        self.invalid = -1
        
    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if num != self.value:
            self.invalid = self.index
        self.index += 1
        if self.index >= self.k and self.invalid < self.index - self.k:
            return True
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
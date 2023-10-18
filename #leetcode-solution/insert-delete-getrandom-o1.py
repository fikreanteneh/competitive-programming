
class RandomizedSet:

    def __init__(self):
        self.nodes = []
        self.indexes = {}
    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        self.indexes[val] = len(self.nodes)
        self.nodes.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.nodes:
            return False
        removedIndex = self.indexes[val]
        self.nodes[removedIndex], self.nodes[-1] = self.nodes[-1], self.nodes[removedIndex]
        self.indexes[self.nodes[removedIndex]] = removedIndex
        self.nodes.pop()
        self.indexes.pop(val)
        
        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.nodes) - 1)
        return self.nodes[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
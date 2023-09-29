class Node:
    def __init__(self):
        self.child = [None]*26
        self.end = False
        self.sum = 0
        self.prev = -1

class Trie:

    def __init__(self):
        self.root = Node()
    
    def charToIndex(self, char):
        return ord(str(char)) - 97
    
    def indexToChar(self, index):
        return chr(index + 97)
    
    def reachNode(self, value, root = None):
        curr = root if root else self.root
        parent, index = curr, -1
        for i, val in enumerate(value):
            index = self.charToIndex(val)
            if curr.child[index] is None:
                return (None, None, -1)
            parent = curr
            curr = curr.child[index]
        return (curr, parent, index)

    def insert(self, key, value, main) -> None:
        curr = self.root
        for i, val in enumerate(key):
            index = self.charToIndex(val)
            curr.sum += value
            if curr.child[index] is None:
                curr.child[index] = Node()
            curr = curr.child[index]
        curr.end = True
        curr.sum += value
        curr.prev = main

class MapSum:

    def __init__(self):
        self.tree = Trie()

    def insert(self, key: str, val: int) -> None:
        (curr, parent, index) = self.tree.reachNode(key)
        added = val
        if curr and curr.end:
            added = -1*curr.prev + val 
        self.tree.insert(key, added, val)
        
    def sum(self, prefix: str) -> int:
        (curr, parent, index) = self.tree.reachNode(prefix)
        if not curr:
            return 0
        return curr.sum
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
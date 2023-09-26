class Node:
    def __init__(self):
        self.child = [None]*26
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()
    
    def charToIndex(self, char):
        return ord(str(char)) - 97

    def insert(self, value: str) -> None:
        curr = self.root
        for i, asciiNum in enumerate(value):
            index = self.charToIndex(asciiNum)
            if curr.child[index] is None:
                curr.child[index] = Node()
            curr = curr.child[index]
        curr.end = True

    def search(self, value: str) -> bool:
        curr = self.root
        for i, val in enumerate(value):
            index = self.charToIndex(val)
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        return curr.end
    
    def startsWith(self, value: str) -> bool:
        curr = self.root
        for i, val in enumerate(value):
            index = self.charToIndex(val)
            if curr.child[index] is None:
                return False
            curr = curr.child[index]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
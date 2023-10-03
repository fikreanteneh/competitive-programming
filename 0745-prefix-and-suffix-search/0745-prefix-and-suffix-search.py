class Node:
    def __init__(self):
        self.child = [None]*27
        self.end = False
        self.lastNode = None
        self.lastIndex = -1

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

    def insert(self, value, wordIndex) -> None:
        curr = self.root
        for i, val in enumerate(value):
            index = self.charToIndex(val)
            if curr.child[index] is None:
                curr.child[index] = Node()
            curr.lastIndex = wordIndex
            curr.lastNode = curr.child[index]
            curr = curr.child[index]
        curr.end = True
        curr.lastIndex = wordIndex

class WordFilter:

    def __init__(self, words: List[str]):
        self.tree = Trie()
        for i, word in enumerate(words):
            for j in range(len(word) - 1, -1, -1):
                self.tree.insert(word[j:] + "{" + word, i)

    def f(self, pref: str, suff: str) -> int:
        word = suff  + "{" + pref
        curr, parent, index = self.tree.reachNode(word)
        if not curr:
            return -1
        return curr.lastIndex
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
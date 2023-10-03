class Node:
    def __init__(self):
        self.child = [None]*26
        self.end = False
        self.count = 0

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

    def insert(self, value) -> None:
        curr = self.root
        for i, val in enumerate(value):
            index = self.charToIndex(val)
            if curr.child[index] is None:
                curr.child[index] = Node()
            curr = curr.child[index]
            curr.count += 1
        curr.end = True
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tree = Trie()
        def find(word):
            sums = 0
            curr = tree.root
            for i, val in enumerate(word):
                index = tree.charToIndex(val) 
                curr = curr.child[index]
                sums += curr.count
            return sums

        for word in words:
            tree.insert(word)
        for i, word in enumerate(words):
            words[i] = find(word)
        return words
        
        
        
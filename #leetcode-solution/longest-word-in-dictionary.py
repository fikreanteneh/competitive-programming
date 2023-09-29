class Node:
    def __init__(self):
        self.child = [None]*26
        self.end = False

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

    def insert(self, value: str) -> None:
        curr = self.root
        for i, val in enumerate(value):
            index = self.charToIndex(val)
            if curr.child[index] is None:
                curr.child[index] = Node()
            curr = curr.child[index]
        curr.end = True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        tree = Trie()
        tree.root.end = True
        for word in words:
            tree.insert(word)
        self.curr = ""
        stack = []
        def dfs(node):
            if not node.end:
                return
            if len(stack) > len(self.curr):
                self.curr = "".join(stack)
            for i, child in enumerate(node.child):
                if child and child.end:
                    stack.append(tree.indexToChar(i))
                    dfs(child)
                    stack.pop()
        dfs(tree.root)
        return self.curr
        
        
        
        
        
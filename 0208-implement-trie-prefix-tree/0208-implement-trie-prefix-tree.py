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
    
    def delete(self, value: str) -> None: 
        curr, parent, index = self.reachNode(value)
        if not curr:
            return
        curr.end = False
        if not any(curr.child):
            parent[index] = None

    def search(self, value: str, root = None) -> bool:
        root = root if root else self.root
        curr, parent, index = self.reachNode(value, root)
        return curr and curr.end
        
    
    def startsWith(self, value: str, root = None) -> bool:
        root = root if root else self.root
        curr, parent, index = self.reachNode(value, root)
        return bool(curr)
        
    
    def fillSearch(self, value, root = None):
        root = root if root else self.root
        curr, parent, index = self.reachNode(value, root)
        answer = []
        parents = []
        if not curr:
            return answer
        def dfs(node):
            if node.end:
                char = value + "".join([self.indexToChar(parent) for parent in parents])
                answer.append(char)
            for index, child in enumerate(node.child):
                if child is None:
                    continue
                parents.append(index)
                dfs(child)
                parents.pop()
        dfs(curr)
        return answer